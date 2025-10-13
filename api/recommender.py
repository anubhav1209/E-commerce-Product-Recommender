import pandas as pd
import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# --- Configuration ---
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'db.sqlite3')
PRODUCTS_TABLE_NAME = 'products'


class Recommender:
    def __init__(self):
        print("DEBUG: Initializing recommender...")
        
        # --- DEBUGGING STEP: Check if DB exists ---
        print(f"DEBUG: Attempting to connect to database at: {DB_PATH}")
        if not os.path.exists(DB_PATH):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(f"FATAL ERROR: Database file not found at {DB_PATH}")
            print("Please ensure 'db.sqlite3' is inside the 'data' folder.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            self.df = pd.DataFrame() # Create empty dataframe to prevent crash
            return
        
        self.df = self._load_product_data()
        
        # --- DEBUGGING STEP: Check if data was loaded ---
        if self.df.empty:
            print("ERROR: Data loading failed. DataFrame is empty. Cannot proceed.")
            return

        self._prepare_data()
        self.cosine_sim = self._compute_similarity_matrix()
        self.indices = pd.Series(self.df.index, index=self.df['product_id']).drop_duplicates()
        print("Recommender initialized successfully.")

    def _load_product_data(self):
        try:
            conn = sqlite3.connect(DB_PATH)
            query = f"SELECT * FROM {PRODUCTS_TABLE_NAME};"
            df = pd.read_sql_query(query, conn)
            conn.close()
            print(f"DEBUG: Successfully loaded {len(df)} products from the database.")
            return df
        except Exception as e:
            print(f"ERROR: An exception occurred while loading data from database: {e}")
            return pd.DataFrame()

    def _prepare_data(self):
        self.df['description'] = self.df['description'].fillna('')
        self.df['category'] = self.df['category'].fillna('')
        self.df['name'] = self.df['name'].fillna('')
        self.df['soup'] = self.df['name'] + ' ' + self.df['category'] + ' ' + self.df['description']
        print("DEBUG: Created 'soup' column for text analysis.")

    def _compute_similarity_matrix(self):
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.df['soup'])
        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        print("DEBUG: Computed cosine similarity matrix.")
        return cosine_sim

    def get_recommendations(self, product_id: str, num_recs: int = 5):
        if not hasattr(self, 'indices') or self.df.empty:
            print("ERROR: Recommender is not properly initialized. Cannot get recommendations.")
            return []

        if product_id not in self.indices:
            print(f"WARNING: Product ID '{product_id}' not found in the dataset.")
            return []

        idx = self.indices[product_id]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:num_recs+1]
        product_indices = [i[0] for i in sim_scores]
        return self.df['product_id'].iloc[product_indices].tolist()


# --- Main execution block for testing ---
if __name__ == '__main__':
    recommender_engine = Recommender()

    # We only run the test if the recommender was initialized with data
    if not recommender_engine.df.empty:
        print("\n--- Testing Recommender ---")
        
        # This is the product_id for a "Solid" t-shirt from our sample data
        test_product_id = 'c2d766ca982eca8304150849735ffef9'
        
        print(f"Getting recommendations for product_id: {test_product_id}")
        recommendations = recommender_engine.get_recommendations(test_product_id, num_recs=5)

        if recommendations:
            print("\nRecommended Product IDs:")
            for rec_id in recommendations:
                print(rec_id)
        else:
            print("\nCould not generate recommendations. Check if the test product ID exists or if there was an error above.")
    else:
        print("\n--- Testing Skipped ---")
        print("Testing was skipped because the recommender could not be initialized with data.")
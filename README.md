# Full-Stack E-commerce Product Recommender 🛍️

This project is a complete, full-stack application that provides intelligent, personalized product recommendations. It features a Streamlit web interface, a FastAPI backend, a hybrid recommendation engine, and leverages a Large Language Model (LLM) for generating dynamic, human-like explanations and product summaries.

---

##  Live Demo

*https://youtu.be/zN-oOIDIQXU*


---

## Key Features

* **Interactive Web Interface:** A user-friendly frontend built with Streamlit to visualize recommendations.
* **Hybrid Recommendation Engine:** Combines two strategies for smart suggestions:
    * **LLM-Powered Query Expansion:** Uses an LLM to brainstorm complementary product categories (e.g., "helmet" for "cycling shorts").
    * **Content-Based Filtering:** Uses TF-IDF and Cosine Similarity to find similar products while filtering out exact duplicates.
* **AI-Powered Explanations & Summaries:** Leverages the Llama 3.1 model via the Groq API to:
    * Generate a unique, friendly explanation for each recommendation.
    * Summarize long product descriptions into concise, appealing blurbs.
* **Decoupled Architecture:** A robust backend API built with FastAPI serves the data, allowing the frontend to remain lightweight and responsive.

---

## Technology Stack

| Component | Technology/Library |
| :--- | :--- |
| **Frontend** | Streamlit |
| **Backend API** | Python, FastAPI, Uvicorn |
| **Recommendation Engine** | Pandas, Scikit-learn, Inflect |
| **LLM Integration** | Groq API (Llama 3.1) |
| **Database** | SQLite |

---

## Setup & Run

**1. Clone the repository:**
```bash
git clone <your-repository-url>
cd product-recommender
```

**2  Create and activate a virtual environment:**
```bash
python -m venv venv
# On Windows
.\venv\Scripts\Activate.ps1
# On macOS/Linux
source venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Add API Key:**
```bash
Get a free API key from Groq.
Paste the key into the API_KEY variable inside api/llm_handler.py
```
**5. Seed the database:**
```bash
python seed_database.py
```
**6. Run the Application:**

Terminal 1 (Backend):
```bash
python -m uvicorn api.main:app --reload
```

Terminal 2 (Frontend):
```bash
streamlit run app.py
```

Navigate to the local URL provided by Streamlit to use the application.



■ System Architecture
The system follows a decoupled, service-oriented architecture ensuring scalability and modularity. Workflow: 1. Streamlit frontend sends user_id to FastAPI backend. 2. Backend retrieves last-viewed product from SQLite. 3. Hybrid Engine applies “Head” (LLM brainstorming) and “Tail” (TF-IDF) strategies. 4. LLM summarizes and explains each recommendation. 5. JSON response sent to frontend for display.

■ Core Features
Hybrid Recommendation Engine: - “Head”: LLM-powered complementary product brainstorming. - “Tail”: TF-IDF-based similar product filtering. - Combined for diversity and relevance. LLM Integration (Groq + Llama 3.1): - Summarization: Condenses verbose product descriptions. - Explanation: Generates user-friendly reasoning for each recommendation.

■ Key Learnings & Challenges
Challenge: Google Cloud Gemini API errors (404 Model Not Found) despite proper setup. Solution: Pivoted to Groq API — reliable, fast, and easy to integrate.

-- Learning: Iterative refinement through multiple testing cycles led to improved accuracy and diversity.

■ Future Improvements
- Add Collaborative Filtering using Surprise library. - Incorporate demographics for personalized results. - Integrate Redis caching to reduce API latency. - Enhance Streamlit UI with filters and dark mode.
  
■ Tech Stack
- Frontend: Streamlit - Backend: FastAPI - Database: SQLite - AI/LLM: Llama 3.1 via Groq API ML: TF-IDF, - Cosine Similarity Language: Python Architecture: Modular, Service-Oriented

■ Key Takeaways
- Integrated LLMs into a practical full-stack application. - Overcame real-world API and infrastructure challenges. - Designed a hybrid recommender system balancing intelligence and diversity. - Developed prompt engineering skills for AI UX.
  
■ Final Reflection
“This project taught me to engineer AI systems that not only predict but communicate. It’s about merging technical precision with empathy — the essence of intelligent design.”


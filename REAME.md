# E-commerce Product Recommender with LLM Explanations

## Objective
This project is a fully functional backend API that provides personalized product recommendations based on user behavior. It combines a content-based recommendation engine with a Large Language Model (LLM) to generate user-friendly explanations for why each product is recommended.

## Demo Video
*A brief video demonstrating the project setup and API in action.*

**(Link to your Loom or YouTube video will go here)**

## Tech Stack
* **Backend:** Python, FastAPI
* **Recommendation Engine:** Pandas, Scikit-learn (TF-IDF & Cosine Similarity)
* **Database:** SQLite
* **LLM Integration:** Ollama with Llama 3 (8B model)
* **API Server:** Uvicorn

## Features
* **Content-Based Recommendations:** Suggests products based on textual similarity of their name, category, and description.
* **LLM-Powered Explanations:** For each recommendation, a local LLM generates a unique, human-readable explanation.
* **RESTful API:** A single, easy-to-use endpoint to fetch recommendations for any user.
* **Persistent Storage:** User interactions and product data are stored in a SQLite database.

## Setup & Installation

**1. Clone the repository:**
```bash
git clone <your-repository-url>
cd product-recommender
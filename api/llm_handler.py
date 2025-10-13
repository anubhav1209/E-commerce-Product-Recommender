import ollama

# --- Configuration ---
# This client connects to the Ollama server running locally on your machine.
try:
    client = ollama.Client()
    client.show('llama3') # Verify that the model is available
    print("Ollama LLM handler configured successfully with model 'llama3'.")
except Exception as e:
    client = None
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(f"!!! CRITICAL: Failed to configure Ollama. Error: {e}")
    print("!!! Make sure the Ollama application is running and you have run 'ollama run llama3' in your terminal.")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


def generate_explanation(source_product: dict, recommended_product: dict) -> str:
    """
    Generates a user-facing explanation for a recommendation using a local Ollama model.
    """
    if not client:
        return "LLM not available. Could not generate explanation."

    # Construct a clear and specific prompt for the local model.
    prompt = prompt = f""" You are an expert e-commerce assistant. A user viewed a product with these details: 
    - Name: '{source_product['name']}'
    - Category: '{source_product['category']}'
    - Description Snippet: '{source_product['description'][:150]}...'
    We are recommending a product with these details:
    - Name: '{recommended_product['name']}'
    - Category: '{recommended_product['category']}'
    - Description Snippet: '{recommended_product['description'][:150]}...'
    Explain in one friendly sentence why this is a good recommendation, highlighting a shared feature or style. Start with "since you like this .....".
"""

    try:
        # Generate the content using the Ollama client
        response = client.chat(
            model='llama3', # Specify the local model to use
            messages=[
                {'role': 'user', 'content': prompt}
            ]
        )
        return response['message']['content'].strip()
    except Exception as e:
        print(f"Error during Ollama LLM call: {e}")
        return "We think you'll like this product based on your recent activity."
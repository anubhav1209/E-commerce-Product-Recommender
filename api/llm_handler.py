from groq import Groq

# --- Configuration ---
# PASTE YOUR GROQ API KEY HERE
API_KEY = "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"

# --- Initialization ---
client = None
if not API_KEY or API_KEY == "YOUR-GROQ-API-KEY":
    print("!!! FATAL ERROR: Groq API key is missing.")
else:
    try:
        client = Groq(api_key=API_KEY)
        print("✅ Groq LLM handler configured successfully.")
    except Exception as e:
        print(f"!!! CRITICAL: Failed to configure Groq client. Error: {e}")


def generate_explanation(source_product: dict, recommended_product: dict) -> str:
    if not client:
        return "Groq LLM was not initialized. Check server startup logs."

    prompt = f"""
    You are an expert e-commerce assistant.
    A user recently viewed '{source_product['name']}'.
    We are recommending '{recommended_product['name']}'.
    Explain why this is a good recommendation in one short, friendly sentence. Start with "Because you viewed...".
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            # This is the correct model name for Llama 3 8B on Groq
            model="llama-3.1-8b-instant",
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error during Groq LLM call: {e}")
        return "We think you'll like this product based on your recent activity."
from langchain_google_genai import ChatGoogleGenerativeAI
import os

def set_llm_model(model_name="gemini-2.0-flash-exp", temperature: float = 0.7):
    return ChatGoogleGenerativeAI(
        model=model_name,  # Note: 'model' not 'model_name'
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=temperature
    )

from langchain_google_genai import ChatGoogleGenerativeAI
import os

def set_llm_model(model_name="gemini-1.5-flash", temperature: float = 0.7):
    temperature = min(max(temperature, 0.0), 1.0)
    
    return ChatGoogleGenerativeAI(
        model=model_name,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=temperature
    )

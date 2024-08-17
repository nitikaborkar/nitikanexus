from langchain_openai.chat_models import ChatOpenAI

def set_llm_model(model_name="gpt-4o-mini", temperature: float = 0.7):
    return ChatOpenAI(model_name=model_name, temperature=temperature)

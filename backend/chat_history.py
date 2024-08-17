from langchain.memory import ConversationTokenBufferMemory

def set_chat_history(model, max_token_limit: int = 3097):
    return ConversationTokenBufferMemory(llm=model, max_token_limit=max_token_limit, return_messages=True)

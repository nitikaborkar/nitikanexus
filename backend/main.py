from backend.model import RAG


def create_rag_instance():
    return RAG(
        docs_dir="docs",# Path to your documents directory
        n_retrievals=4,           # Number of documents to retrieve
        chat_max_tokens=3097,     # Maximum number of tokens for chat memory
        creativeness=1.2          # Creativity level for responses
    )

#print("\n Hiya! 🌟 I’m NitikaNexus 🤖, your go-to AI for all things Nitika! Whether you're curious about her work, her favorite Netflix shows, or just want to know what she’s up to when she’s not coding away—ask away! Let’s get started! 🚀 Type 'exit' to exit the program.")

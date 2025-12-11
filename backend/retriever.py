import os
from backend.document_loader import get_docs_list
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def set_retriever(model, docs_dir, k, search_type="similarity", score_threshold=None):

    documents = (docs_dir)
    
    # Split documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    
    # Generate embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=os.getenv("GOOGLE_API_KEY"))

    # Initialize FAISS vector store
    db = FAISS.from_documents(texts, embeddings)
    
    # Choose the appropriate retriever method
    if search_type == "similarity":
        retriever = db.as_retriever(search_kwargs={"k": k})
    elif search_type == "mmr":
        retriever = db.as_retriever(search_type="mmr", search_kwargs={"k": k})
    elif search_type == "similarity_score_threshold":
        if score_threshold is not None:
            retriever = db.as_retriever(
                search_type="similarity_score_threshold", 
                search_kwargs={"score_threshold": score_threshold, "k": k}
            )
        else:
            raise ValueError("score_threshold must be provided for similarity_score_threshold search type.")
    else:
        raise ValueError(f"Unknown search_type: {search_type}")
    
    return retriever

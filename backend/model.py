from llm_model import set_llm_model
from document_loader import get_docs_list
from retriever import set_retriever
from chat_history import set_chat_history
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_core.prompts import MessagesPlaceholder

class RAG:
    def __init__(self,
                 docs_dir: str,
                 n_retrievals: int = 4,
                 chat_max_tokens: int = 3097,
                 model_name="gpt-4o-mini",
                 creativeness: float = 0.7):

        # Initialize the LLM model
        self.__model = set_llm_model(model_name, creativeness)
        
        # Load the documents
        self.__docs_list = get_docs_list(docs_dir)
        
        # Set up the retriever with the model and documents
        self.__retriever = set_retriever(self.__model, self.__docs_list, k=n_retrievals)

        # Initialize chat history management
        self.__chat_history = set_chat_history(self.__model, max_token_limit=chat_max_tokens)

    def ask(self, question: str) -> str:
        # Create a chat prompt template with the appropriate placeholders


        prompt = ChatPromptTemplate.from_messages([
            ("system", "ou are an intelligent assistant designed to provide detailed information about Nitika. Your task is to answer questions clearly and accurately, using the most relevant details from a collection of documents about Nitika's life, experiences, qualifications, and projects. Whether the user refers to you as 'Nitika', 'her', or 'you', all references should be understood as pertaining to Nitika. \n{context}\n\nIf the context does not directly answer the question, provide your best attempt to infer the answer or suggest additional queries to help the user find what they need."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "User's question: {input}"),
        ])
   

        # Initialize the output parser
        output_parser = StrOutputParser()

        # Create the chain of operations
        chain = prompt | self.__model | output_parser

        # Retrieve the documents based on the query
        retrieved_docs = self.__retriever.invoke(question)
        # Extract the text content from the retrieved documents
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])
        # Prepare the input for the chain
        input_data = {
            "input": question,
            "chat_history": self.__chat_history.load_memory_variables({})['history'],
            "context": context
        }
        # Invoke the chain to get the answer
        answer = chain.invoke(input_data)
        # Save the chat context for future interactions
        self.__chat_history.save_context({"input": question}, {"output": answer})
        return answer
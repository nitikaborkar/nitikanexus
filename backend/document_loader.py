from langchain_community.document_loaders import DirectoryLoader, TextLoader

def get_docs_list(docs_dir: str) -> list:
    """
    Load and split documents from a directory.
    :param docs_dir: Directory containing documents to load
    :return: List of split document chunks
    """

    # Loader configuration
    text_loader_kwargs = {'autodetect_encoding': True}
    
    # Initialize DirectoryLoader with TextLoader
    loader = DirectoryLoader(
        docs_dir,
        recursive=True,
        show_progress=True,
        use_multithreading=True,
        max_concurrency=4,
        loader_cls=TextLoader,
        loader_kwargs=text_loader_kwargs
    )

    # Load and split the documents
    return loader.load_and_split()
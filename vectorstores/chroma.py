from LangChainJ.documents import Document
import uuid

class Chroma:
    _LANGCHAIN_DEFAULT_COLLECTION_NAME = "langchain"

    def __init__(
            self,
            collection_name: str = _LANGCHAIN_DEFAULT_COLLECTION_NAME,
            embedding_function = None,
            persist_directory:str|None = None,
            client_settings = None,
            client = None
    ) -> None:
        try:
            import chromadb
            import chromadb.config
        except ImportError as error:
            raise error

        if client is not None:
            self.clint_settings = client_settings
            self.client = client
        else:
            # if client_settings:
            #     client_settings.persist_directory = (
            #         persist_directory or client_settings.persist_directory
            #     )
            if persist_directory is None:
                # chromadb in-memory mod
                self.clint_settings = chromadb.config.Settings(
                    chroma_db_impl="duckdb+parquet",
                )
            else:
                self.clint_settings = chromadb.config.Settings(
                    chroma_db_impl="duckdb+parquet",
                    persist_directory=persist_directory
                )

            # self.clint = chromadb.Client(self.clint_settings)
            self.clint = chromadb.Client()

        self.embedding_function = embedding_function
        self.collection = self.clint.get_or_create_collection(
            name=collection_name,
            # embedding_function=None
        )
    
    def add_text(
            self,
            text:str|Document,
            id = None
        ) -> list[str]:
        """
        Run more texts through the embeddings and add to the vectorstore
        """
        if type(text) == Document:
            text = text.page_content

        if id is None:
            id = str(uuid.uuid4())
        # embeddings = None
        # if self.embedding_function is not None:
        #     embeddings = self.embedding_function.get_embedding(text)
        
        self.collection.upsert(
            # embeddings=embeddings,
            documents=[text],
            ids=[id]
        )

    @classmethod
    def from_texts(
        cls,
        texts: list[str],
        # embedding = None,
        ids = None,
        collection_name: str = _LANGCHAIN_DEFAULT_COLLECTION_NAME,
        persist_directory = None,
    ):
        chroma_collection = cls(
            collection_name=collection_name,
            # embedding_function=embedding,
            persist_directory=persist_directory
        )
        if ids is None:
            ids = [str(uuid.uuid4()) for _ in texts]
        for text, id in zip(texts, ids):
            chroma_collection.add_text(text, id)

        return chroma_collection


    @classmethod
    def from_documents(
        cls,
        documents: list[Document],
        # embedding = None,
        ids = None,
        collection_name: str = _LANGCHAIN_DEFAULT_COLLECTION_NAME,
        persist_directory = None
    ):
        texts = [doc.page_content for doc in documents]
        return cls.from_texts(
            texts=texts,
            # embedding=embedding,
            ids=ids,
            collection_name=collection_name,
            persist_directory=persist_directory
        )

    def delete(self, ids) -> None:
        self.collection.delete(ids=ids)

    def get_query(self, text:str, n_result:int=5):
        return self.collection.query(query_texts=[text], n_results=n_result)['documents'][0]
    
    def as_retriever(self, text:str, n_result:int=5):
        from LangChainJ.openai.openai_module import OpenAIJ
        question_format = "Based on the following statements, answer the question: \n"
        tag = "#Keyword"
        query_list = self.get_query(text, n_result)
        
        for idx in range(len(query_list)):
            question_format = question_format + f"{tag}{idx+1} = {query_list[idx]}\n"
        
        question_format = question_format + f"Question : {text}"
        return OpenAIJ().predict(question_format)
    
    def __len__(self) -> int:
        return self.collection.count()
    
if __name__ == "__main__":
    from LangChainJ.document_loaders import PDFLoader
    print(Chroma.from_texts(
        PDFLoader(".\\LangChainJ\\test_file\\dsci_06_데이터_시각화.pdf").load_and_split(chunk_size=300)
    # ).get_query("tell me what is mpg", 5))
    ).as_retriever("tell me what is mpg", 5))
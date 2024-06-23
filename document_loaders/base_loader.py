from abc import ABC
from LangChainJ.documents import Document

class BaseLoader(ABC):
    def load(self) -> Document:
        pass

    def load_and_split(self, separators:list[str]=["\n\n", "\n", " ", ""], chunk_size:int=100):
        try:
            from LangChainJ.text_splitters import RecursiveCharacterTextSplitter
        except ImportError as error:
            raise ImportError(f"{error}")
        
        text_splitter = RecursiveCharacterTextSplitter(separators, chunk_size)
        doc = self.load()
        return text_splitter.split_text(doc)
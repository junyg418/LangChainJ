from abc import ABC
from LangChainJ.documents import Document

class BaseLoader(ABC):
    def load(self) -> Document:
        pass

    def load_and_split(self):
        try:
            from LangChainJ.text_splitters.character_text_splitter import CharacterTextSplitter
        except ImportError as error:
            raise ImportError(f"{error}")
        
        text_splitter = CharacterTextSplitter()
        doc = self.load()
        return text_splitter.split_text(doc.page_content)
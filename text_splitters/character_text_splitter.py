from LangChainJ.documents import Document
import re

class CharacterTextSplitter:
    def __init__(self, 
                 separator: str = "\n\n",
                #  chunk_size: int = 500,
                 ) -> None:
        self.separator = separator

    def split_text(self, text:str) -> list[Document]:
        if self.separator:
            splits:list[str] = re.split(self.separator, text)
        else:
            splits:list[str] = list(text)
        return [Document(data) for data in splits if data != ""]
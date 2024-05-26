from LangChainJ.documents import Document
import re

class CharacterTextSplitter:
    def __init__(self, 
                 separator: str = "\n\n",
                #  chunk_size: int = 500,
                 ) -> None:
        self.separator = separator

    def split_text(self, text:str):
        if self.separator:
            splits = re.split(self.separator, text)
        else:
            splits = list(text)
        return [data for data in splits if data != ""]
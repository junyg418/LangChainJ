from LangChainJ.document_loaders.base_loader import BaseLoader
from LangChainJ.documents import Document
import os

class HTMLLoader(BaseLoader):
    def __init__(self, path:str) -> None:
        try:
            import bs4
        except ImportError:
            raise ImportError("bs4 is not installed\nPlease write on the commend line > pip install bs4")

        input_path_extension:str = os.path.splitext(path)[1]
        if input_path_extension != ".html":
            raise NameError("The file extension is not .html")
        self.path = path


    def load(self) -> Document:
        from bs4 import BeautifulSoup, FeatureNotFound
        
        with open(self.path, "r", encoding="utf-8") as file:
            try:
                soup = BeautifulSoup(file, "lxml")
            except FeatureNotFound:
                raise ImportError(
                    "lxml parser is not installed\nPlease write on the commend line > pip install lxml"
                )
        html_str:str = soup.get_text()
        return Document(html_str)

if __name__ == "__main__":
    print(repr(HTMLLoader("c:\\temp\\LangChainJ\\test_file\\akaka.html").load_and_split()))
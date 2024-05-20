from LangChainJ.document_loaders.base_loader import BaseLoader
import os

class HTMLLoader(BaseLoader):
    def __init__(self, path:str) -> None:
        try:
            import bs4
        except ImportError:
            raise ImportError("bs4 is not installed\nPlease write on the commend line > pip install bs4")

        self.path = path


    def load(self) -> str:
        from bs4 import BeautifulSoup, FeatureNotFound

        extension:str = os.path.splitext(self.path)[1]
        if extension != ".html":
            raise NameError("The file extension is not .html")
        
        with open(self.path, "r", encoding="utf-8") as file:
            try:
                soup = BeautifulSoup(file, "lxml")
            except FeatureNotFound:
                raise ImportError(
                    "lxml parser is not installed\nPlease write on the commend line > pip install lxml"
                )
        html_str:str = soup.get_text()
        return html_str

if __name__ == "__main__":
    print(repr(HTMLLoader("c:\\temp\\akaka.html").load()))
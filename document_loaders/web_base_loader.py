from LangChainJ.document_loaders import BaseLoader
from LangChainJ.documents import Document, check_module




class WebBaseLoader(BaseLoader):
    def __init__(self, web_path:str) -> None:
        try:
            check_module("bs4")
            check_module("requests")
            check_module("lxml")
        except ModuleNotFoundError as error:
            raise ModuleNotFoundError(error)

        self.web_path = web_path

    def load(self) -> Document:
        from bs4 import BeautifulSoup
        import requests
        
        request = requests.get(self.web_path)
        request.raise_for_status()
        
        soup = BeautifulSoup(request.text, 'lxml')
        result = soup.get_text()
        return Document(result)
    
if __name__ == "__main__":
    url = "https://rfriend.tistory.com/847"
    loader = WebBaseLoader(url)
    print(loader.load_and_split())
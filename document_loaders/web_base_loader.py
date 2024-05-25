from LangChainJ.document_loaders.base_loader import BaseLoader

def check_module(module:str):
    try:
        __import__(module)
    except ImportError:
        raise ModuleNotFoundError(f"{module} is not installed\nPlease write on the commend line > pip install {module}")

class WebBaseLoader(BaseLoader):
    def __init__(self, web_path:str) -> None:
        try:
            check_module("bs4")
            check_module("requests")
            check_module("lxml")
        except ModuleNotFoundError as error:
            raise ModuleNotFoundError(error)

        self.web_path = web_path

    def load(self):
        from bs4 import BeautifulSoup
        import requests
        
        request = requests.get(self.web_path)
        request.raise_for_status()
        
        soup = BeautifulSoup(request.text, 'lxml')
        return soup.get_text()
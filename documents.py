class Document:
    page_content:str
    def __init__(self, page_content) -> None:
        self.page_content = page_content
    
    def __str__(self) -> str:
        return self.page_content
    
    def __repr__(self) -> str:
        return repr(self.page_content)
    
    def __len__(self) -> int:
        return len(self.page_content)
    
def check_module(module:str):
    try:
        __import__(module)
    except ImportError:
        raise ModuleNotFoundError(f"{module} is not installed\nPlease write on the commend line > pip install {module}")
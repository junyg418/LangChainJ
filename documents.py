class Document:
    page_content:str
    def __init__(self, page_content) -> None:
        self.page_content = page_content
    
    def __str__(self) -> str:
        return self.page_content
    
    def __repr__(self) -> str:
        return self.page_content
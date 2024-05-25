from LangChainJ.document_loaders.base_loader import BaseLoader
import os

class PDFLoader(BaseLoader):
    def __init__(self, path:str):
        try:
            import pypdf
        except ImportError:
            raise ImportError("pypdf is not installed\nPlease write on the commend line > pip install pypdf")
      
        input_path_extension:str = os.path.splitext(path)[1]
        if input_path_extension != ".pdf":
            raise NameError("The file extension is not .pdf")
        self.path = path

    def load(self) -> str:
        from pypdf import PdfReader

        reader:PdfReader = PdfReader(self.path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        
        return text
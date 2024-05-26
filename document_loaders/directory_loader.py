from LangChainJ.document_loaders.base_loader import BaseLoader
from LangChainJ.documents import Document
import importlib
import os

def is_sup(input_glob:str, glob_sup:str) -> bool:
    return (input_glob == glob_sup) or (input_glob == f'.{glob_sup}')

def modify_extension(extension:str):
    """
    before the extension. A function that removes
    """
    return f"{extension[1:]}" if extension[0] == '.' else extension

class DirectoryLoader(BaseLoader):
    def __init__(self,
                 path:str,
                 glob:str=".txt") -> None:
        """
        This class reads files that exist in a directory.\n
        :param path:
            receives the path to the file\n
        :param glob:
            extension of the file.\n
            Only .pdf, .html, and .txt extension types are supported.
        """
        self.path = path
        is_support:bool = is_sup(glob, "pdf") or is_sup(glob, "html") or is_sup(glob, "txt")
        if (not is_support): raise NotImplementedError(f"{glob} is not supported")
        self.glob = glob

        input_path_extension:str = os.path.splitext(self.path)[1]
        if input_path_extension != f"{self.glob}" if self.glob[0] == '.' else f".{self.glob}":
            raise NameError(f"The file extension is not {self.glob}")
        self.path = path


    def load(self) -> Document:
        if is_sup(self.glob, "txt"):
            result_str = []
            with open(self.path, "r", encoding="utf-8") as file:
                while True:
                    line = file.readline()
                    result_str.append(line)
                    if not line: break

            result_str = ''.join(result_str)
            return Document(result_str)
        
        else:
            module_name = f"{modify_extension(self.glob)}_loader"
            module_dict = {"html_loader":"HTMLLoader", "pdf_loader":"PDFLoader"}
            module = importlib.import_module(f"LangChainJ.document_loaders.{module_name}")
            print(module)
            LoaderClass:BaseLoader = getattr(module, module_dict[module_name])
            
            return LoaderClass(self.path).load()
        

if __name__ == "__main__":
    print(repr(DirectoryLoader("c:\\temp\\LangChainJ\\test_file\\test.txt", ".txt").load()))
    # print(DirectoryLoader("c:\\temp\\LangChainJ\\test_file\\akaka.html", ".html").load())
    # print(DirectoryLoader("c:\\temp\\LangChainJ\\test_file\\dsci_06_데이터_시각화.pdf", ".pdf").load())
    pass
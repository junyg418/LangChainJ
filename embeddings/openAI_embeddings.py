from chromadb.api.types import Embeddings
from LangChainJ.documents import Document, check_module
from chromadb import EmbeddingFunction
import os

class OpenAIEmbeddings(EmbeddingFunction):
    def __init__(self):
        try:
            check_module("openai")
            # check_module("numpy")
        except ImportError as error:
            raise ImportError(error)

    def get_embedding(self, text:Document|str, open_ai=None, model="text-embedding-3-small"):
        if open_ai is None:
            from openai import OpenAI
            open_ai = OpenAI()
        if type(text) == Document:
            text = text.page_content
        text = text.replace("\n", " ")
        result = open_ai.embeddings.create(input=text, model=model)
        return result
    
    def embed_documents(self, texts:list[Document|str], model="text-embedding-3-small"):
        from openai import OpenAI
        openai = OpenAI()
        
        if (api_key :=os.getenv("OPENAI_API_KEY")) is not None:
            openai.api_key = api_key
        else:
            raise EnvironmentError("The 'OPENAI_API_KEY' environment variable is not set. Please add your OpenAI API key to the environment variables or check if the spelling is correct.")

        result = [self.get_embedding(text, openai) for text in texts]
        return result
    
    # def __call__(self, input: Any) -> List[Sequence[float] | Sequence[int]]:
    #     return super().__call__(input)


# def normalize_l2(input_text):
#     import numpy as np
#     input_text = np.array(input_text)
#     if input_text.ndim == 1:
#         norm = np.linalg.norm(input_text)
#         if norm == 0:
#             return input_text
#         return input_text / norm
#     else:
#         norm = np.linalg.norm(input_text, 2, axis=1, keepdims=True)
#         return np.where(norm == 0, input_text, input_text / norm)
        
if __name__ == "__main__":
    print(OpenAIEmbeddings().embed_documents(['\n\n', 'punctuation. If you are paid hourly, please estimate an equivalent yearly salary. If you\n\n', 'prefer not to answer, please leave the box empty.\n', 'What is your current total annual compensation (salary, bonuses, and perks, before', '\ntaxes and deductions)? Please enter a whole number in the box below, without any']))
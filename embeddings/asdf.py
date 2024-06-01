from LangChainJ.documents import Document

class OpenAIEmbeddings:
    def __init__(self):
        try:
            import openai
            import numpy
        except ImportError:
            raise ImportError("openai is not installed\nPlease write on the commend line > pip install openai")

    def embed_documents(self, texts:list[Document], model="text-embedding-3-small"):
        from openai import OpenAI
        openai = OpenAI()
        openai.embeddings.create(input=texts, model=model, encoding_format=float)
    

    def get_embedding(self, text:list[Document]):
        pass
        

    def normalize_l2(self, input_text):
        import numpy as np
        input_text = np.array(input_text)
        if input_text.ndim == 1:
            norm = np.linalg.norm(input_text)
            if norm == 0:
                return input_text
            return input_text / norm
        else:
            norm = np.linalg.norm(input_text, 2, axis=1, keepdims=True)
            return np.where(norm == 0, input_text, input_text / norm)
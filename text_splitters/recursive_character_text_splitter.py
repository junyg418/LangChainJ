from LangChainJ.documents import Document
import re

class RecursiveCharacterTextSplitter:
    def __init__(self, 
                 separators:list[str]=["\n\n", "\n", " ", ""],
                 chunk_size: int = 100
                ) -> None:
        self.separators = separators
        self.chunk_size = chunk_size

    def split_text(self, texts:Document|str):
        if type(texts) == Document:
            temp_texts = texts.page_content
        good_chunk_len = 0
        final_chunk = []
        good_chunk = []
        bad_chunk = [temp_texts]

        def append_good_chunk(text:str) -> None:
            nonlocal good_chunk
            nonlocal good_chunk_len

            good_chunk.append(text)
            good_chunk_len += len(text)

        def _split_text_with_separator(text:Document, separator:str) -> list[str]:
            if separator:
                splits = re.split(f"({separator})", text)
            else:
                splits = list(text)
            return [data for data in splits if data != ""]
        
        for idx, separator in enumerate(self.separators[:4]):
            good_chunk_len = 0
            run_bad_chunk = bad_chunk.copy()
            bad_chunk = []
            for text in run_bad_chunk:
                if len(text) <= self.chunk_size:
                    good_chunk.append(text)
                else:
                    bad_chunk.extend(_split_text_with_separator(text, separator))

                [append_good_chunk(chunk) for chunk in bad_chunk if len(chunk) <= self.chunk_size]
                bad_chunk = [chunk for chunk in bad_chunk if len(chunk) > self.chunk_size]
                
                if len(good_chunk) == 0: continue
                if len(good_chunk) == 1:
                    final_chunk.append(good_chunk[0])
                    good_chunk = []
                    continue

                before_final = [good_chunk[0]]
                good_chunk_len += len(good_chunk[0])
                for g_text in good_chunk[1:]:
                    if len(g_text) + good_chunk_len <= self.chunk_size:
                        good_chunk_len += len(g_text)
                        before_final.append(g_text)
                    else:
                        final_chunk.append("".join(before_final))
                        before_final = [g_text]
                        good_chunk_len = len(g_text)
                        
                
                final_chunk.append("".join(before_final))
                good_chunk = []
                
        final_chunk = [Document(text) for text in final_chunk]
        final_chunk = self.instend_embed_TEST(final_chunk)
        return final_chunk
    
    def instend_embed_TEST(self, texts:list[Document]) -> Document:
        result = [text for text in texts if text.page_content not in self.separators]
        return result


if __name__ == "__main__":
    text = """What is your current total annual compensation (salary, bonuses, and perks, before
taxes and deductions)? Please enter a whole number in the box below, without any

punctuation. If you are paid hourly, please estimate an equivalent yearly salary. If you

prefer not to answer, please leave the box empty.
"""
    print(f"fin_result = {RecursiveCharacterTextSplitter().split_text(Document(text))}")
    # print(repr(text))
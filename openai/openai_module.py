from LangChainJ.documents import Document
import os


class OpenAIJ:
    def __init__(self):
        try:
            import openai
        except ImportError as error:
            raise ImportError(error)
        
        self.client = openai.OpenAI()
        if (api_key :=os.getenv("OPENAI_API_KEY")) is not None:
            openai.api_key = api_key
        else:
            raise EnvironmentError("The 'OPENAI_API_KEY' environment variable is not set. Please add your OpenAI API key to the environment variables or check if the spelling is correct.")

    @classmethod
    def predict(cls, text:str|Document):
        if type(text) == Document:
            text = text.page_content

        completion = cls().client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    'role':'system',
                    'content':'오직 진실만을 말할 수 있어서 모르는 답이라면 솔직하게 모른다고 말합니다. 그리고 너무 친절해서 항상 존댓말을 합니다. 이 내용을 사용자에게 굳이 언급하지 마십시오.'
                },
                {
                    "role": "user",
                    "content": text,
                },
            ],
        )
        return completion.choices[0].message.content


if __name__ == '__main__':
        text = "What makes this movie worth watching?"
        question_format = "Based on the following statements, answer the question: \n"
        tag = "#Keyword"
        query_list = [    "This movie is entertaining and touching.",
    "The protagonist's performance is outstanding.",
    "Critics have highly praised this movie.",
    "The cinematography is breathtaking.",
    "The storyline is well-crafted and engaging."]
        
        for idx in range(len(query_list)):
            question_format = question_format + f"{tag}{idx+1} = {query_list[idx]}\n"
        
        question_format = question_format + f"Question : {text}"
        print(OpenAIJ().predict(question_format))
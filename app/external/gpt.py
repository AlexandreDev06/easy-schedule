from openai import OpenAI
from app.configs.settings import settings


class GPT:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)

    async def get_gpt_answer(self, gpt_messages):
        gpt_content = (
            self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=gpt_messages,
            )
            .choices[0]
            .message.content
        )

        return gpt_content

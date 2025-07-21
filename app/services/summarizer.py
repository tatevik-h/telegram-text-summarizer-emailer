import openai
from app.config import config

openai.api_key = config.OPENAI_API_KEY


def summarize_text(text: str) -> str:
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "You summarize texts."},
                    {"role": "user", "content": text}
                ],
                max_token=150,
                temperature=0.5,
            )
            return response.choices[0].message.content.strip()


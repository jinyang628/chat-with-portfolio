from google import genai

import os

from app.utils.singleton import Singleton


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the environment or .env file")

SYSTEM_PROMPT = "You are a helpful assistant."
USER_PROMPT = "{user_input}"


class LlmClient(metaclass=Singleton):
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = "gemini-2.0-flash-exp"

    def generate(self, user_input: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=[SYSTEM_PROMPT, USER_PROMPT.format(user_input=user_input)],
        )
        return response.text

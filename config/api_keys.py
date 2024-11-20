import os
from dotenv import load_dotenv

class APIKeys:
    def __init__(self):
        load_dotenv()
        self.openai_key = os.getenv('OPENAI_API_KEY')
        self.anthropic_key = os.getenv('ANTHROPIC_API_KEY')
        self.google_key = os.getenv('GOOGLE_API_KEY')

    def validate_keys(self):
        keys = {
            'OpenAI': self.openai_key,
            'Anthropic': self.anthropic_key,
            'Google': self.google_key
        }
        return {name: bool(key) for name, key in keys.items()}

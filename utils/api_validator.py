import os
from dotenv import load_dotenv

class APIValidator:
    @staticmethod
    def validate_openai_key(key):
        """Validate OpenAI API key format"""
        return key and key.startswith('sk-') and len(key) > 40

    @staticmethod
    def validate_anthropic_key(key):
        """Validate Anthropic API key format"""
        return key and key.startswith('sk-ant-') and len(key) > 50

    @staticmethod
    def validate_google_key(key):
        """Validate Google API key format"""
        return key and len(key) > 30

    @classmethod
    def validate_all_keys(cls):
        """
        Validate all API keys from environment
        Returns:
            Dict with validation status for each key
        """
        load_dotenv()
        return {
            'OpenAI': cls.validate_openai_key(os.getenv('OPENAI_API_KEY')),
            'Anthropic': cls.validate_anthropic_key(os.getenv('ANTHROPIC_API_KEY')),
            'Google': cls.validate_google_key(os.getenv('GOOGLE_API_KEY'))
        }
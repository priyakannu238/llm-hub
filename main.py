import gradio as gr
from config.api_keys import APIKeys
from models.model_handler import ModelsHandler  # Add this import
from models.openai_model import OpenAIModel
from models.anthropic_model import AnthropicModel
from models.google_model import GoogleModel
from ui.chat_interface import ChatInterface
from utils.logger import setup_logging

def main():
    # Setup logging
    logger = setup_logging()
    
    # Initialize API keys
    api_keys = APIKeys()
    key_status = api_keys.validate_keys()
    
    # Initialize models
    models_handler = ModelsHandler(api_keys)
    
    # Create and launch interface
    chat_interface = ChatInterface(models_handler)
    interface = chat_interface.build_interface()
    interface.launch(share=False)

if __name__ == "__main__":
    main()
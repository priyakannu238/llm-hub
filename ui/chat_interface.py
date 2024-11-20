import gradio as gr
import asyncio
from config.settings import MODEL_CONFIGS
from personalities.system_messages import PERSONALITIES


class ChatInterface:
    def __init__(self, models_handler):
        self.models_handler = models_handler

    def build_interface(self):
        with gr.Blocks() as interface:
            model_dropdown = gr.Dropdown(
                choices=list(MODEL_CONFIGS.keys()),
                label="Select Model",
                value="GPT-4o"
            )
            personality_dropdown = gr.Dropdown(
                choices=list(PERSONALITIES.keys()),
                label="Select Personality",
                value="General Assistant"
            )
            custom_personality = gr.Textbox(
                label="Custom System Message (Optional)",
                placeholder="Enter custom instructions for the AI..."
            )
            
            chatbot = gr.ChatInterface(
                fn=lambda message, history, model_name, personality, custom_system_message: asyncio.run(
                    self.models_handler.handle_chat(
                        message, 
                        history, 
                        model_name=model_name, 
                        personality=personality, 
                        custom_system_message=custom_system_message
                    )
                ),
                additional_inputs=[model_dropdown, personality_dropdown, custom_personality]
            )
        return interface
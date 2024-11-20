import asyncio
from config.settings import MODEL_CONFIGS
from models.openai_model import OpenAIModel
from models.anthropic_model import AnthropicModel
from models.google_model import GoogleModel
from personalities.system_messages import PERSONALITIES


class ModelsHandler:
    def __init__(self, api_keys):
        self.api_keys = api_keys
        self.models = MODEL_CONFIGS
        self._initialize_models()

    def _initialize_models(self):
        for model_name, config in MODEL_CONFIGS.items():
            provider = config['provider']
            system_message = 'You are a helpful assistant'

            # Dynamically initialize models based on the provider
            if provider == 'openai' and self.api_keys.openai_key:
                self.models[model_name] = OpenAIModel(
                    model_name=config['model_name'],
                    system_message=system_message,
                    api_key=self.api_keys.openai_key,
                )
            elif provider == 'anthropic' and self.api_keys.anthropic_key:
                self.models[model_name] = AnthropicModel(
                    model_name=config['model_name'],
                    system_message=system_message,
                    api_key=self.api_keys.anthropic_key,
                )
            elif provider == 'google' and self.api_keys.google_key:
                self.models[model_name] = GoogleModel(
                    model_name=config['model_name'],
                    system_message=system_message,
                    api_key=self.api_keys.google_key,
                )

    async def handle_chat(self, message, history, model_name='GPT-4o', personality='General Assistant', custom_system_message=None):
        # Ensure model_name exists in available models
        if model_name not in self.models:
            # Fallback to first available model if requested model is not found
            model_name = list(self.models.keys())[0]
        
        # Determine system message
        if custom_system_message:
            system_message = custom_system_message
        else:
            system_message = PERSONALITIES.get(personality, PERSONALITIES['General Assistant'])
        
        # Select model
        model = self.models[model_name]
        model.system_message = system_message
        
        # Generate response
        response = ''
        async for chunk in model.generate_response(message, history):
            response = chunk
        
        return response


# # models/model_handler.py
# import asyncio
# from config.settings import MODEL_CONFIGS
# from models.openai_model import OpenAIModel
# from models.anthropic_model import AnthropicModel
# from models.google_model import GoogleModel
# from personalities.system_messages import PERSONALITIES

# class ModelsHandler:
#     def __init__(self, api_keys):
#         self.api_keys = api_keys
#         self.models = {}
#         self._initialize_models()

#     def _initialize_models(self):
#         # OpenAI Models
#         if self.api_keys.openai_key:
#             self.models['GPT-4o'] = OpenAIModel(
#                 model_name='gpt-4o', 
#                 system_message='You are a helpful assistant', 
#                 api_key=self.api_keys.openai_key
#             )
#             self.models['GPT-3.5'] = OpenAIModel(
#                 model_name='gpt-3.5-turbo', 
#                 system_message='You are a helpful assistant', 
#                 api_key=self.api_keys.openai_key
#             )
        
#         # Anthropic Models
#         if self.api_keys.anthropic_key:
#             self.models['Claude-3'] = AnthropicModel(
#                 model_name='claude-3-opus-20240229', 
#                 system_message='You are a helpful assistant', 
#                 api_key=self.api_keys.anthropic_key
#             )
        
#         # Google Models
#         if self.api_keys.google_key:
#             self.models['PaLM'] = GoogleModel(
#                 model_name='gemini-pro', 
#                 system_message='You are a helpful assistant', 
#                 api_key=self.api_keys.google_key
#             )

#     async def handle_chat(self, message, history, model_name='GPT-3.5', personality='General Assistant', custom_system_message=None):
#         # Ensure model_name exists in available models
#         if model_name not in self.models:
#             # Fallback to first available model if requested model is not found
#             model_name = list(self.models.keys())[0]
        
#         # Determine system message
#         if custom_system_message:
#             system_message = custom_system_message
#         else:
#             system_message = PERSONALITIES.get(personality, PERSONALITIES['General Assistant'])
        
#         # Select model
#         model = self.models[model_name]
#         model.system_message = system_message
        
#         # Generate response
#         response = ''
#         async for chunk in model.generate_response(message, history):
#             response = chunk
        
#         return response
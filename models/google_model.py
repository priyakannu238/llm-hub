import google.generativeai as genai
from .base_model import BaseModel

class GoogleModel(BaseModel):
    def __init__(self, model_name, system_message, api_key):
        super().__init__(model_name, system_message)
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name=model_name,
            system_instruction=system_message
        )

    async def generate_response(self, message, history):
        # Prepare conversation history
        chat_history = [
            {
                'role': 'user' if msg.get('role') == 'user' else 'model', 
                'parts': [msg['content']]
            } for msg in history
        ]
        
        # Start chat with history
        chat = self.model.start_chat(history=chat_history)
        
        # Generate response
        response = chat.send_message(message)
        
        # Simulate streaming
        yield response.text



# # models/google_model.py
# import vertexai
# from vertexai.language_models import ChatModel
# from .base_model import BaseModel

# class GoogleModel(BaseModel):
#     def __init__(self, model_name, system_message, project_id, api_key=None):
#         super().__init__(model_name, system_message)
#         vertexai.init(project=project_id)
#         self.chat_model = ChatModel.from_pretrained(self.model_name)

#     async def generate_response(self, message, history):
#         # Convert history to context string for PaLM
#         context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in history])
#         full_context = f"{context}\nSystem: {self.system_message}\nUser: {message}"
        
#         chat = self.chat_model.start_chat(
#             context=full_context,
#             max_output_tokens=4096
#         )
        
#         # Generate response streaming isn't directly supported, so we'll simulate
#         response = chat.send_message(message)
#         yield response.text
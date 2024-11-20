from anthropic import Anthropic
from .base_model import BaseModel

class AnthropicModel(BaseModel):
    def __init__(self, model_name, system_message, api_key):
        super().__init__(model_name, system_message)
        self.client = Anthropic(api_key=api_key)

    async def generate_response(self, message, history):
        # Prepare messages, converting to Anthropic's expected format
        messages = history + [{"role": "user", "content": message}]
        
        stream = self.client.messages.create(
            model=self.model_name,
            max_tokens=4096,
            system=self.system_message,
            messages=messages,
            stream=True
        )

        response = ""
        for chunk in stream:
            if chunk.type == 'content_block_delta':
                response += chunk.delta.text
                yield response
from openai import OpenAI
from .base_model import BaseModel

class OpenAIModel(BaseModel):
    def __init__(self, model_name, system_message, api_key):
        super().__init__(model_name, system_message)
        self.client = OpenAI(api_key=api_key)

    async def generate_response(self, message, history):
        # Validate and sanitize the history
        formatted_history = []
        for entry in history:
            if isinstance(entry, dict) and "role" in entry and "content" in entry:
                formatted_history.append({"role": entry["role"], "content": entry["content"]})
            else:
                # Optionally log or handle invalid history entries
                print(f"Invalid history entry: {entry}")

        # Construct the messages list
        messages = [
            {"role": "system", "content": self.system_message}
        ] + formatted_history + [
            {"role": "user", "content": message}
        ]

        # Stream response from OpenAI API
        try:
            stream = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                stream=True
            )
            response = ""
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    response += chunk.choices[0].delta.content
                    yield response
        except Exception as e:
            print(f"Error during OpenAI API call: {e}")
            yield "An error occurred while processing your request."




# # models/openai_model.py
# from openai import OpenAI
# from .base_model import BaseModel

# class OpenAIModel(BaseModel):
#     def __init__(self, model_name, system_message, api_key):
#         super().__init__(model_name, system_message)
#         self.client = OpenAI(api_key=api_key)

#     async def generate_response(self, message, history):
#         messages = [
#             {"role": "system", "content": self.system_message}
#         ] + history + [
#             {"role": "user", "content": message}
#         ]

#         stream = self.client.chat.completions.create(
#             model=self.model_name,
#             messages=messages,
#             stream=True
#         )

#         response = ""
#         for chunk in stream:
#             if chunk.choices[0].delta.content:
#                 response += chunk.choices[0].delta.content
#                 yield response

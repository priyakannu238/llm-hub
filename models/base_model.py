from abc import ABC, abstractmethod

class BaseModel(ABC):
    def __init__(self, model_name, system_message):
        self.model_name = model_name
        self.system_message = system_message

    @abstractmethod
    async def generate_response(self, message, history):
        pass

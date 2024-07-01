from .api_keys import anthropic_api_key
from anthropic import Anthropic

class Chat:
    def __init__(self):
        self.client = Anthropic(api_key=anthropic_api_key)
        self.messages = []
        self.temperature = 0.7
        self.max_tokens = 500
        self.system_instructions = 'you are a useful bot'

    def add_message(self, role, content):
        self.messages.append({'role': role, 'content': content})

    def stream_chat(self, prompt_content):
        self.add_message('user', prompt_content)
        with self.client.messages.stream(
            model="claude-3-5-sonnet-20240620",
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            system=self.system_instructions,
            messages=self.messages
        ) as stream:
            full_response = ""
            for chunk in stream:
                if chunk.type == "content_block_delta":
                    text = chunk.delta.text
                    yield text
                    full_response += text
        self.add_message('assistant',[{"type":"text","text": full_response}])

    def clear_history(self):
        self.messages.clear()

    def get_history(self):
        return self.messages

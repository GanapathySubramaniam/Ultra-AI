from .api_keys import anthropic_api_key
from anthropic import Anthropic

client = Anthropic(api_key=anthropic_api_key)

def prompt_gen(task):
    with open('./prompts/prompt_generator.txt') as metaprompt_file:
        metaprompt=metaprompt_file.read()
    prompt = metaprompt.replace("{{TASK}}", task)
    assistant_partial = "<Inputs>"
    messages=[
            {
                "role": "user",
                "content":  prompt
            },
            {
                "role": "assistant",
                "content": assistant_partial
            }
        ]
    with client.messages.stream(
                                    model="claude-3-5-sonnet-20240620",
                                    max_tokens=4096,
                                    messages=messages,
                                    temperature=0
                                )as stream:
        full_response = ""
        for chunk in stream:
            if chunk.type == "content_block_delta":
                text = chunk.delta.text
                yield text
                full_response += text
    return full_response
          


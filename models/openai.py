from openai import OpenAI
import requests
from PIL import Image
import io
import functools

from .api_keys import openai_api_key
client=OpenAI(api_key=openai_api_key)

def tts(prompt):
    file_name='tts.mp3'
    male_response = client.audio.speech.create(model="tts-1",voice='onyx',input=str(prompt[0]['text']))
    male_response.write_to_file(f'{file_name}')
    return file_name


@functools.lru_cache(maxsize=100)
def tts2(prompt):
    response = client.audio.speech.create(
        model="tts-1-hd",  # Using a faster, more efficient model
        voice='nova',
        input=str(prompt),
        speed=1  
    )
    return response.content

def convert_to_rgba(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    rgba_image = image.convert('RGBA')
    byte_arr = io.BytesIO()
    rgba_image.save(byte_arr, format='PNG')
    return byte_arr.getvalue()

def download_image(image_url):
    response = requests.get(image_url)
    response.raise_for_status() 
    return convert_to_rgba(response.content)


def transcribe_audio(audio_bytes):
        try:
            audio_file = io.BytesIO(audio_bytes)
            audio_file.name = 'audio.wav'  
            transcript = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file
            )
            return transcript.text
        except Exception as e:
            return f"An error occurred during transcription: {str(e)}"


class image_gen_model:
    def __init__(self):
        self.openai_client=OpenAI(api_key=openai_api_key)
        self.revised_prompt=[]
        self.size="1024x1024"
        self.quality="standard"
        self.history=[]
        self.style='natural' 
        self.edit_image_size='1024x1024'
        self.images=[]

    def add_message(self,role,content,content_type):
        self.history.append({'role':role,'content':content,'type':content_type})

    def generate_image(self,prompt):
        response = self.openai_client.images.generate(
                                                model="dall-e-3",
                                                prompt=prompt,
                                                size=self.size,
                                                quality=self.quality,
                                                style=self.style,
                                                n=1,
                                                response_format='url')
        image_url = response.data[0].url                                        
        self.images.append(download_image(image_url))
        revised_prompt=response.data[0].revised_prompt
        self.revised_prompt.append(revised_prompt)
        return image_url,revised_prompt
    
    def edit_image(self,prompt):
        response=self.openai_client.images.edit(image=self.images[-1],
                                                prompt=prompt,
                                                size=self.edit_image_size,
                                                n=1,
                                                response_format='url')
                                            
        image_url = response.data[0].url  
        self.images.append(download_image(image_url))  
        revised_prompt=response.data[0].revised_prompt
        self.revised_prompt.append(revised_prompt)
        return image_url,revised_prompt
        
    def image_chat(self,prompt):
        self.add_message('user',prompt,'text')
        if len(self.history)>=2:
                prompt=f'#Original Prompt {self.revised_prompt[-1]} #Edit  {prompt}'
        image,revised_prompt=self.generate_image(prompt)
        self.add_message('assistant',image,'image')
        self.add_message('assistant',revised_prompt,'text')

    def clear_history(self):
        self.history.clear()


class ChatGPT:
    def __init__(self):
        self.client = OpenAI(api_key=openai_api_key)
        self.messages = []
        self.temperature = 0.7
        self.max_tokens = 50
        self.system_instructions = 'You are a concise and quick-responding AI assistant.'

    def add_message(self, role, content):
        self.messages.append({'role': role, 'content': content})

    def stream_chat(self, prompt_content):
        self.add_message('user', prompt_content)
        stream = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": self.system_instructions}] + self.messages,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            stream=True
        )
        
        full_response = ""
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                text = chunk.choices[0].delta.content
                yield text
                full_response += text
        
        self.add_message('assistant', full_response)

    def clear_history(self):
        self.messages.clear()

    def get_history(self):
        return self.messages
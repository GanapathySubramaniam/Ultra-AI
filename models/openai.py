from openai import OpenAI
import requests
from PIL import Image
import io

from .api_keys import openai_api_key
client=OpenAI(api_key=openai_api_key)

def tts(prompt):
    file_name='tts.mp3'
    male_response = client.audio.speech.create(model="tts-1",voice='onyx',input=str(prompt[0]['text']))
    male_response.write_to_file(f'{file_name}')
    return file_name


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
        if len(self.history)>2:
                prompt=f'#Original Prompt {self.revised_prompt[-1]} #Edit  {prompt}'
        image,revised_prompt=self.generate_image(prompt)
        self.add_message('assistant',image,'image')
        self.add_message('assistant',revised_prompt,'text')

    def clear_history(self):
        self.history.clear()

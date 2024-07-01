from openai import OpenAI
from .api_keys import openai_api_key
client=OpenAI(api_key=openai_api_key)

def tts(text):
    file_name='tts.mp3'
    male_response = client.audio.speech.create(model="tts-1",voice='onyx',input=str(text))
    male_response.write_to_file(f'{file_name}')
    return file_name

class image_gen_model:
    def __init__(self):
        self.openai_client=OpenAI(api_key=openai_api_key)
        self.revised_prompt=[]
        self.size="1024x1024"
        self.quality="standard"
        self.history=[]

    def add_message(self,role,content,content_type):
        self.history.append({'role':role,'content':content,'type':content_type})

    def generate_image(self,prompt):
        response = self.openai_client.images.generate(
                                                model="dall-e-3",
                                                prompt=prompt,
                                                size=self.size,
                                                quality=self.quality,
                                                n=1,
                                                )

        image_url = response.data[0].url
        revised_prompt=response.data[0].revised_prompt
        self.revised_prompt.append(revised_prompt)
        return image_url,revised_prompt

    def image_chat(self,prompt):
        if len(self.history)==0:
            self.add_message('user',prompt,'text')
            image_url,revised_prompt=self.generate_image(prompt)
            self.add_message('assistant',image_url,'image')
            self.add_message('assistant',revised_prompt,'text')

        else:
            prompt=f'#PREVIOUS REVISED PROMPT \n {self.revised_prompt[-1]} \n#ADJUSTMENTS:\n{prompt}'
            image_url,revised_prompt=self.generate_image(prompt)
            self.add_message('assistant',image_url,'image')
            self.add_message('assistant',revised_prompt,'text')

    def clear_history(self):
        self.history.clear()
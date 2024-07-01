from openai import OpenAI
from .api_keys import openai_api_key
client=OpenAI(api_key=openai_api_key)
def tts(text):
    file_name='tts.mp3'
    male_response = client.audio.speech.create(model="tts-1",voice='onyx',input=str(text))
    male_response.write_to_file(f'{file_name}')
    return file_name
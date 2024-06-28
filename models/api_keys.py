import os 
from dotenv import load_dotenv

load_dotenv('models/.env')

anthropic_api_key=os.environ['ANTHROPIC']
openai_api_key=os.environ['OPENAI']

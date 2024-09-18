import openai
from openai import OpenAI
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

API_KEY = os.environ['apiKey']
# openai.api_key  = os.getenv('apiKey')
client = OpenAI(api_key=API_KEY)

def get_completion(prompt, model="gpt-4o"):
    messages = [{"role": "user", "content": prompt}]
    # response = openai.ChatCompletion.create(
    #     model=model,
    #     messages=messages,
    #     temperature=0, # this is the degree of randomness of the model's output
    # )
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content
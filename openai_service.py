import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def call_open_ai(messages):
    client = OpenAI()
    response = client.chat.completions.create(
        temperature = 1,
        model = "gpt-4o-mini",
        # messages = [
        #     {"role" : "system", "content" : "you are a chatbot. answer the questions in a manner as if you're teaching a 5 year old"},
        #     {"role" : "user", "content" : question}
        # ]s
        messages = messages

    )

    # print(response)

    return response.choices[0].message.content

# answer = call_openai("what's 2+2?")
# print(answer)
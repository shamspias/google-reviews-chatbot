import openai
from config.settings import OPENAI_API_KEY


def generate_response_gpt3(message_list):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                     {"role": "system",
                      "content": "You are an AI named sonic and you are in a conversation with a human. You can answer "
                                 "questions, provide information, and help with a wide variety of tasks."},
                     {"role": "user", "content": "Who are you?"},
                     {"role": "assistant",
                      "content": "I am the sonic powered by ChatGpt.Contact me sonic@deadlyai.com"},
                 ] + message_list
    )

    return response["choices"][0]["message"]["content"].strip()


def generate_code_response(message_text):
    response = openai.Completion.create(
        model="code-davinci-003",
        prompt=message_text,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response["choices"][0]["text"].strip()

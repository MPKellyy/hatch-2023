import openai
import re
import os
#import load_dotenv from dotenv
import requests

#load_dotenv()

# Set up the OpenAI API credentials
openai.api_key = os.getenv("key")

# Define a function to translate text
"""
def translate_text(input_text):
    # Define the prompt for the API request
    prompt = f"Translate the following scientific text into simple terms:\n\n{input_text}\n\nTranslation:"
    # Send the prompt to the API and get the response
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    # Extract the translated text from the response
    translated_text = response.choices[0].text
    # Clean up the translated text by removing any leading/trailing whitespace and line breaks
    translated_text = translated_text.strip().replace('\n', ' ')
    # Remove any extra white space in the text
    translated_text = re.sub(' +', ' ', translated_text)
    # Return the translated text
    return translated_text
    """


def api_test():
    # Set up the API endpoint URL and your API key
    url = "https://api.openai.com/v1/engine/chat/generic"
    api_key = openai.api_key

    # Set up the request headers with the API key
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    # Set up the request body with the message you want to generate a response for
    data = {
        "prompt": "Hello, how are you?",
        "temperature": 0.5,
        "max_tokens": 16,
    }

    # Make the API request and print the response
    response = requests.post(url, headers=headers, json=data)
    print(response.json())


import openai
import re
import os
#import
import requests

#load_dotenv()

# Set up the OpenAI API credentials
openai.api_key = "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"

# Define a function to translate text

def translate_text(input_text):
    # Define the prompt for the API request
    prompt = f"Explain the following scientific concept as if I were a kindergartener:\n\n{input_text}\n\nTranslation:"
    # Send the prompt to the API and get the response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=1,
    )
    # Extract the translated text from the response
    translated_text = response.choices[0].text
    # Clean up the translated text by removing any leading/trailing whitespace and line breaks
    translated_text = translated_text.strip().replace('\n', ' ')
    # Remove any extra white space in the text
    translated_text = re.sub(' +', ' ', translated_text)
    # Return the translated text
    return translated_text

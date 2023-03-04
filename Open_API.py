import openai
import re
import os
import requests
from parser import *


# Set up the OpenAI API credentials
openai.api_key = "INSERT KEY"


def summarize_paper(input_text):
    prompt = f"Translate the following scientific text into simple terms:\n\n{input_text}\n\nTranslation:"
    return translate_text(prompt)


def convert_to_tweet(input_text):
    prompt = f"Turn the following text into a tweet under 280 characters:\n\n{input_text}\n\nTranslation:"
    return translate_text(prompt)


# Define a function to translate text
def translate_text(prompt):
    # Send the prompt to the API and get the response
    response = openai.Completion.create(
        engine="text-davinci-003",
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


def display_response_to_console(response):
    response = re.findall(r"[^.!?]+[.!?]", response)

    for sentence in response:
        print(sentence)


def summarize_paper_test():
    # Wang_QC_Recognition_of_camouflage_targets_with_hyper-spectral_polarization_imaging_system.pdf
    # Zhai_H_Infrared_polarization_detection_method_for_weak_target_in_sky_background.pdf
    pdf = get_text_from_pdf("Zhai_H_Infrared_polarization_detection_method_for_weak_target_in_sky_background.pdf")

    for page in pdf:
        response = summarize_paper(page)
        display_response_to_console(response)


def convert_to_tweet_test():
    response = convert_to_tweet(get_text_from_pdf("meeting_notes.pdf"))
    display_response_to_console(response)


# summarize_paper_test()
convert_to_tweet_test()


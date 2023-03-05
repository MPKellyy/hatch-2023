import openai
import re
import os
#import load_dotenv from dotenv
import requests
from parser import *

#load_dotenv()

# Set up the OpenAI API credentials
openai.api_key = "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"


def summarize_paper(input_text):
    prompt = f"Translate the following scientific text into simple terms:\n\n{input_text}\n\nTranslation:"
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


def simplify_paper_test():
    #################################################
    # Wang_QC_Recognition_of_camouflage_targets_with_hyper-spectral_polarization_imaging_system.pdf
    # Zhai_H_Infrared_polarization_detection_method_for_weak_target_in_sky_background.pdf
    # response = translate_text("My name is Michael. I am a college student. My favorite color is green.")
    pdf = get_text_from_pdf("Zhai_H_Infrared_polarization_detection_method_for_weak_target_in_sky_background.pdf")

    for page in pdf:
        response = summarize_paper(page)
        response = response.split(". ")
        for sentence in response:
            if sentence[len(sentence) - 1] != ".":
                sentence += "."
            print(sentence)
        print("\n")
    #################################################


def generate_text_on_topic(topic, modifier):
    prompt = f"Explain {topic} to me {modifier}."
    return translate_text(prompt)


def generate_social_media_post(post_type, topic):
    prompt = f"Write me a moderately sized {post_type} about {topic} with detail."
    return translate_text(prompt)


def generate_script(topic):
    prompt = f"Write me a presentation script about {topic} in detail with explanations."
    return translate_text(prompt)

#generate email
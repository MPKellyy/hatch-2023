import openai
import re
import os
import requests
from parser import *


# Set up the OpenAI API credentials
openai.api_key = "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"


def find_terms_paper(filename):
    input_text = ""
    for page in get_text_from_pdf(filename):
        input_text += page + " "
    prompt = f"Find key terms in this text (if any) and define them:\n\n{input_text}\n\nTranslation:"
    return translate_text(prompt)


def summarize_paper(filename):
    input_text = ""
    for page in get_text_from_pdf(filename):
        input_text += page + " "
    prompt = f"Translate the following scientific text into simple terms:\n\n{input_text}\n\nTranslation:"
    return translate_text(prompt)


def convert_to_post(filename):
    input_text = ""
    for page in get_text_from_pdf(filename):
        input_text += page + " "
    # prompt = f"Turn the following text into a {media_name} post:\n\n{input_text}\n\nTranslation:"
    # TODO revisit this
    prompt = f"Turn the following text into a social media post:\n\n{input_text}\n\nTranslation:"
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
    response = re.findall(r"[^:.!?]+[:.!?]", response)

    for sentence in response:
        print(sentence)


def summarize_paper_test(filename):
    pdf = get_text_from_pdf(filename)

    for page in pdf:
        response = summarize_paper(page)
        display_response_to_console(response)
        print("")


# def convert_to_post_test(filename):
    # social_media = ["twitter", "instagram", "facebook", "linkedin"]

    # for platform in social_media:
        # print(platform + ":")
        # response = convert_to_post(platform, get_text_from_pdf(filename)[0])
        # display_response_to_console(response)


def find_key_terms_paper_test(filename):
    response = find_terms_paper(get_text_from_pdf(filename)[0])
    display_response_to_console(response)
    return translate_text(response)


# summarize_paper_test("Zhai_H_Infrared_polarization_detection_method_for_weak_target_in_sky_background.pdf")
# convert_to_post_test("meeting_notes.pdf")
# find_key_terms_paper_test("meeting_notes.pdf")
# print(convert_to_post("facebook", "My birthday"))


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
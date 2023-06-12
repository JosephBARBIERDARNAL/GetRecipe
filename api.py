import openai
import requests
import streamlit as st
from PIL import Image


def api_gpt(prompt, system_msg, temperature=1, top_p=1, frequency_penalty=1, presence_penalty=1):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{"role": "system", "content": system_msg},
                                                        {"role": "user", "content": prompt}],
                                              temperature=temperature,
                                              top_p=top_p,
                                              frequency_penalty=frequency_penalty,
                                              presence_penalty=presence_penalty)
    output = completion["choices"][0]["message"]["content"]
    return output


def api_dalle(prompt, n=2):
    with st.spinner("Loading"):
        response = openai.Image.create(
            prompt=prompt,
            n=n,
            size="1024x1024")
        image_url1 = response['data'][0]['url']
        image_url2 = response['data'][1]['url']

        #Save the image
        image_data1 = requests.get(image_url1).content
        image_data2 = requests.get(image_url2).content
    return image_data1, image_data2

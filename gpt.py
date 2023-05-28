import openai
import streamlit as st

@st.cache_data()
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
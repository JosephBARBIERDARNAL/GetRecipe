import streamlit as st
import openai
from gpt import api_gpt
from front import make_space

st.title("From ingredients to recipes")
make_space(3)

#define key
openai.api_key = "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"

system_msg = """You are an AI assistant that helps people find recipes based on ingredients they have at home.
                All recipes you suggest should be extremely original and tasty. Also, all your answers must have
                humor and jokes."""
prompt = st.text_area("Enter your question")
output = None
if len(prompt)>5:
    output = api_gpt(prompt, system_msg)
    st.write(output)
    make_space(1)
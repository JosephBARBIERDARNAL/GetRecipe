import streamlit as st
import re

@st.cache_data()
def get_last_sentence(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    last_sentence = sentences[-1].strip()
    return last_sentence
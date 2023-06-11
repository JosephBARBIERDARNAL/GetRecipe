import streamlit as st
import pandas as pd
from io import StringIO
import re

def make_space(n):
    for _ in range(n):
        st.write("")


@st.cache_data()
def csv_string_to_df(csv_string):
    csv_data = StringIO(csv_string)
    df = pd.read_csv(csv_data)
    return df


@st.cache_data()
def count_words(string):
    word_regex = r'\b\w+\b'
    word_count = len(re.findall(word_regex, string))
    return word_count
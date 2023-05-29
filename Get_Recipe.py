import streamlit as st
from api import api_gpt, api_dalle
import openai
from front import make_space

st.title("From ingredients to Recipes")
make_space(3)

#define key
openai.api_key = st.secrets["openai_key"]

#define the pre-prompts
system_msg = """You're a funny AI assistant who helps people find original recipes using the ingredients they have at home.
                All the recipes you propose must be extremely original and tasty. You have to adapt to the user's preferences
                (vegan, gluten-free, lactose-free etc, if specified). In addition, all your answers must contain humor and jokes."""
system_msg_summary = """Describe in one sentence the meal created by describing precisely what it should look like"""

#get user input
prompt = st.text_area("Enter your ingredients and (optionnaly) some preferences")
prompt = "User ingredients: " + prompt + "\n\nAI assistant: "

#call gpt api and display output
output_gpt = None
run = st.button("Find a recipe!")
if run and len(prompt) > 5:
    output_gpt = api_gpt(prompt, system_msg)
    st.write(output_gpt)
    make_space(1)


    #call dalle api and display output
    input_dalle = api_gpt(output_gpt, system_msg_summary)
    input_dalle = "4k detailed and high quality photo of " + input_dalle[17:].lower()
    st.write("Input Dall-e: ", input_dalle)
    make_space(1)
    st.markdown("### Generated picture of the recipe")

    #call dalle api and display output
    api_dalle(input_dalle)



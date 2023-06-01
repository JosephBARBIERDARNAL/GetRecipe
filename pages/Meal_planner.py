import streamlit as st
import openai
import base64

from api import api_gpt
from front import make_space
from ingredients import ingredients


st.title("Meal Planner")
make_space(3)

#define gpt parameters
openai.api_key = st.secrets["openai_key"]
system_msg_summary = """You're a funny AI assistant who creates a meal plan for a week.
                        All the meals you propose must be extremely tasty. Your answers
                        must be in a csv format with the following columns: day, meal, recipe.
                        Your answers must only be composed of 2 meals per day: lunch and dinner.
                        Your answer are only the CSV file, no need to write anything else."""

#Get user input
use_predefined_ingredients = st.checkbox("Use pre-defined ingredients", value=False)
if not use_predefined_ingredients:
    prompt = st.text_area("Enter your preferences")
else:
    ingredients_list = ingredients()
    prompt = st.multiselect("Select your ingredients", ingredients_list)
    prompt = [string[0].upper() + string[1:] for string in prompt]
    number_of_ingredients = len(prompt)
    prompt = ", ".join(prompt)
    st.write(f"You have {number_of_ingredients} ingredients:\n\n {prompt}")


#call gpt api and display output
output_gpt = None
run = st.button("Find a meal plan!")
if run and len(prompt) > 5:
    output_gpt = api_gpt(prompt, system_msg_summary)
    make_space(1)

    #download csv
    csv = output_gpt.encode()
    b64 = base64.b64encode(csv).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="meal_plan.csv">Download my meal plan</a>'
    st.markdown(href, unsafe_allow_html=True)








# user ingredient suggestion by mail
make_space(15)
st.markdown("An ingredient is missing? Send me an email and I will add it to the list!")
st.markdown("joseph.barbierdarnal@gmail.com")

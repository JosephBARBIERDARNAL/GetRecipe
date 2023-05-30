import streamlit as st
import openai
from api import api_gpt
from front import make_space
import base64

st.title("Meal Planner")

#define gpt parameters
openai.api_key = st.secrets["openai_key"]
system_msg_summary = """You're a funny AI assistant who creates a meal plan for a week.
                        All the meals you propose must be extremely tasty. Your answers
                        must be in a csv format with the following columns: day, meal, recipe.
                        Your answers must only be composed of 2 meals per day: lunch and dinner.
                        Your answer are only the CSV file, no need to write anything else."""

#Get user input
prompt = st.text_area("Enter your preferences")

#call gpt api and display output
output_gpt = None
run = st.button("Find a meal plan!")
if run and len(prompt) > 5:
    output_gpt = api_gpt(prompt, system_msg_summary)
    st.write(output_gpt)
    make_space(1)

    #download csv
    csv = output_gpt.encode()
    b64 = base64.b64encode(csv).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="meal_plan.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)




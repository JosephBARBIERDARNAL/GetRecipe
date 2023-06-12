import streamlit as st
import openai
from api import api_gpt, api_dalle
from front import make_space
import base64
import requests

st.title("From ingredients to Recipes")
st.markdown("""##### This app generates recipes and pictures of the meals based on the ingredients you have at home. You can use the "Find a recipe" button several times to get different ideas.""")
make_space(3)

#define key
openai.api_key = st.secrets["openai_key"]

#define the pre-prompts
system_msg = """You're a funny AI assistant who helps people find original recipes using the ingredients they have at home.
                All the recipes you propose must be extremely original and tasty. You have to adapt to the user's preferences
                (meat-free, vegan, gluten-free, lactose-free etc, if specified by the user). In addition, all your answers must
                contain humor and jokes."""
system_msg_summary = """Describe in one sentence the meal created by describing precisely how it should look like"""

#get user inputs
meal_type = st.selectbox("What is your mood?", ["Surprise me", "I want to eat clean", "Pig out mood"])
prompt = st.text_area("Enter your ingredients and (optionally) some preferences")
prompt = "User mood is: " + meal_type + "\n\n" + "User ingredients: " + prompt + "\n\nAI assistant: "

#call gpt api and display output
output_gpt = None
run = st.button("Find a recipe!")
def api_dalle(prompt, output_gpt, init_input_dalle, n=2):
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
        col1, col2 = st.columns(2)
        with col1:
            st.image(image_data1, caption="Generated image, DALL•E", use_column_width=True)
        with col2:
            st.image(image_data2, caption="Generated image, DALL•E", use_column_width=True)

        # allow the user to save the recipe and picture in an html file (recipe first, then picture)
        html = output_gpt + "<br><br>" + init_input_dalle[16:] + "<br><br><br><img src='data:image/png;base64,{}'>".format(base64.b64encode(image_data1).decode())
        b64 = base64.b64encode(html.encode()).decode()
        href = f'<a href="data:text/html;base64,{b64}" download="recipe.html">Download my recipe</a>'
        st.markdown(href, unsafe_allow_html=True)
if run and len(prompt) > 5:
    output_gpt = api_gpt(prompt, system_msg)
    st.write(output_gpt)
    make_space(1)

    #call dalle api and display output
    init_input_dalle = api_gpt(output_gpt, system_msg_summary)
    input_dalle = "4k detailed and high quality photo of " + init_input_dalle[16:].lower()
    make_space(1)
    st.markdown("### Generated picture of the recipe")
    api_dalle(input_dalle, output_gpt, init_input_dalle)





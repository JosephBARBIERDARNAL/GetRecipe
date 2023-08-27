import openai
import requests
import streamlit as st
import base64


def api_gpt(prompt, system_msg, temperature=1, top_p=1, frequency_penalty=1, presence_penalty=1):
    with st.spinner("Loading"):
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{"role": "system", "content": system_msg},
                                                        {"role": "user", "content": prompt}],
                                              temperature=temperature,
                                              top_p=top_p,
                                              frequency_penalty=frequency_penalty,
                                              presence_penalty=presence_penalty)
        output = completion["choices"][0]["message"]["content"]
    return output


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

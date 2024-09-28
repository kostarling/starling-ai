import streamlit as st
from st_app_lib import *
from g4f.client import Client

question = st.text_input("Q")

client = Client()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", 
               "content": f"Tell a shocking fact short story in 250 words about: {question}. Start with the words Did you know that"}]
)

st.markdown(response.choices[0].message.content)

print(response.choices[0].message.content)
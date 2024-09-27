
import streamlit as st
import requests
from st_app_lib import *


HF = st.secrets["HF"]
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
headers = {"Authorization": f"Bearer {HF}"}
prompt = st.text_input(label="PROMPT", value="Gilgamesh")
title = dna_gpt(f"Write 3 words title for youtube thumbnail of {prompt}")
super_prompt = dna_gpt(f"""
Write a prompt to generate a youtube thumbnail about: {prompt}. 
Make the prompt less than 100 words. 
The details and colors of the image should appeal to a young audience. 
The prompt begins with the phrase: A youtube thumbnail about {prompt}
The prompt should include a description of a person with a shocked expression and bulging eyeballs.
The prompt ends with the phrase: The youtube thumbnail includes the words {title} using a catchy design.
Note: Make sure {title} is in uppercase
""")

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": super_prompt
})

st.image(image_bytes)

hyper_prompt = st.text_input(label="HYPER FLUX", value="Gilgamesh")
from gradio_client import Client

client = Client("ByteDance/Hyper-FLUX-8Steps-LoRA")
result = client.predict(
		height=768,
		width=1024,
		steps=8,
		scales=3.5,
		prompt=super_prompt,
		seed=3413,
		api_name="/process_image"
)
print(result)
st.image(result)
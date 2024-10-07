import streamlit as st
import streamlit.components.v1 as components

import requests

tts_text = st.text_area("TTS", "Hello world")

response = requests.post(
    "https://simple-api.glif.app",
    json={"id": "cm1ziq4ev000o3r5zzgh7ys39", "inputs": [f'{tts_text}']},
    headers={"Authorization": "e4dd1fe277dd37fd82a0bc2be65ace75"},
)
print(response.content)

import json
data = json.loads(response.content) 


st.audio(data['output'])

import streamlit as st
from st_app_lib import *
from g4f.client import Client

from youtube_transcript_api import YouTubeTranscriptApi


question = st.text_input("Q", value="2J4chT7jX0Q")

trans = gpt4o("get transcribe of this video: https://www.youtube.com/watch?v=2J4chT7jX0Q")

st.markdown(trans)

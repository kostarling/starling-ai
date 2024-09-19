import streamlit as st
import asyncio
from st_app_lib import txt2img, dna_gpt
from prompts import *

RUNWARE_API_KEY = st.secrets["RUNWARE_API_KEY"]

col1, col2 = st.columns(2)

design = col1.text_input(label="book cover design", value="flovers and birds")
cover_text = col2.text_input(label="book cover text", value="flovers and birds")



Generate_Book_button = st.button('Generate Book Cover')


col_cover_im, col_description = st.columns(2)

cover_im = col_cover_im.image("https://im.runware.ai/image/ws/0.5/ii/9c3f8e19-e661-446b-ae74-356cbd6e8dc8.jpg")

description = col_description.markdown(BOOK_DESCRIPTION)

Prompt = f"""
            Book cover design with {design} and text in center "{cover_text}"
            """
description_prompt = f"""
            Write markdown KDP book Title, Subtitle and descriptin about {design} and "{cover_text}"
            Example:
            {BOOK_DESCRIPTION}
            """

if Generate_Book_button:
    result = asyncio.run(txt2img(RUNWARE_API_KEY, Prompt))
    cover_im.image(result)
    description.markdown(dna_gpt(description_prompt))

    
    
import streamlit as st
from st_app_lib import *
import asyncio

from moviepy.editor import *
from random import choice
import numpy as np
import cv2
from PIL import Image
import requests

RUNWARE_API_KEY = st.secrets["RUNWARE_API_KEY"]

Short_Title = st.text_input(label="YT Short Title", value="Thor, the mighty god of Asgard")

title = dna_gpt(f"Write 3 words title for youtube thumbnail of {Short_Title}")
super_prompt = dna_gpt(f"""
Write a prompt to generate a youtube thumbnail about: {Short_Title}. 
Make the prompt less than 100 words. 
The details and colors of the image should appeal to a young audience. 
The prompt begins with the phrase: A youtube thumbnail about {Short_Title}
The prompt should include a description of a person with a shocked expression and bulging eyeballs.
The prompt ends with the phrase: The youtube thumbnail includes the words {title} using a catchy design.
Note: Make sure {title} is in uppercase
""")

YTthumbnail = asyncio.run(t2i(RUNWARE_API_KEY, super_prompt, height=704, width=1280, numberResults=1))
YTthumbnail_pil = Image.open(requests.get(YTthumbnail[0], stream=True).raw)
YTthumbnail_pil.save(".temp/YTthumbnail.jpg")
YTthumbnail_st = st.image(".temp/YTthumbnail.jpg", caption="Youtube Thumbnail")

Short_Story = gpt4o(f"Tell a shocking fact wery long story (minimum 20000 simbols) about: {Short_Title}. Start with the words Did you know that")

st.text_area(label="Short Story", value=Short_Story)

asyncio.run(tts(Short_Story))
st.audio(".temp/test.mp3")


Generate_button = st.button('Generate YT Video')

if Generate_button:

    YTStitle = dna_gpt(f"Make a good title for Youtube short video about {Short_Story}")
    YTSdescription = dna_gpt(f"Make a good description for Youtube short video about {Short_Story}")
    YTSkeywords = dna_gpt(f"Make a 10 keywords for Youtube short video about {Short_Story}, write only coma separated text.")
    "TITLE"
    st.code(YTStitle, language="python")
    "DESCRIPTION"
    st.code(YTSdescription, language="python")
    "KEYWORDS"
    st.code(YTSkeywords, language="python")

    Prompt = dna_gpt(f"Make a good promt (max 70 tokens) for drawing fotorealistic HD 4K with epic detailed background, medieval: {Short_Story}")
    imagesURLs = asyncio.run(t2i(RUNWARE_API_KEY, Prompt, height=768, width=1280, numberResults=5))
    #imagesURLs = asyncio.run(t2i(RUNWARE_API_KEY, Prompt, height=512, width=512, numberResults=10))
    st.image(imagesURLs, width=50)
            

    audio_clip = AudioFileClip(f".temp/test.mp3").volumex(1.2)

    bg_audio_clip = AudioFileClip(f".temp/bgm.MP3").volumex(1)

    final_audio_clip = CompositeAudioClip([audio_clip, bg_audio_clip.set_duration(audio_clip.duration)])

    imgs = [Image.open(requests.get(iu, stream=True).raw) for iu in imagesURLs]
    pil_imgs_im = [ImageClip(np.array(im)).set_duration(audio_clip.duration / len(imgs)) for im in imgs]
    position = ['center', 'left', 'right', 'topleft', 'topright'] #['center', 'bottom', 'left', 'right', 'topleft', 'topright', 'bottomleft', 'bottomright']
    zoom_imgs = [Zoom(icic.set_fps(24), mode=choice(["in","out"]),position=choice(position),speed=4) for icic in pil_imgs_im]
    zoom_imgs = [zi.fadein(.2).fadeout(.2) for zi in zoom_imgs]
    final_clip = concatenate_videoclips(zoom_imgs, method='compose').set_audio(final_audio_clip)
    final_clip.write_videofile(f'.temp/test.mp4', fps=1)

    st.video('.temp/test.mp4', start_time=2)

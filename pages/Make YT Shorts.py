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

Generate_button = st.button('Generate YT Short Video')

if Generate_button:
    Short_Story = gpt4o(f"Tell a shocking fact short story in 160 words about: {Short_Title}. Start with the words Did you know that")

    st.text_area(label="Short Story", value=Short_Story)

    asyncio.run(tts(Short_Story))
    st.audio(".temp/test.mp3")


    YTStitle = dna_gpt(f"Make a good title for Youtube short video about {Short_Story}")
    YTSdescription = dna_gpt(f"Make a good description for Youtube short video about {Short_Story}")
    YTSkeywords = dna_gpt(f"Make a 10 keywords for Youtube short video about {Short_Story}, write only coma separated text.")
    "TITLE"
    st.code(YTStitle, language="python")
    "DESCRIPTION"
    st.code(YTSdescription, language="python")
    "KEYWORDS"
    st.code(YTSkeywords, language="python")

 


    Prompt = gpt4o(f"Make a good promt (max 70 tokens) for drawing fotorealistic HD 4K with epic detailed background, medieval: {Short_Story}")
    imagesURLs = asyncio.run(txt2img_shorts(RUNWARE_API_KEY, Prompt))
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
    final_clip.write_videofile(f'.temp/test.mp4', fps=24)

    st.video('.temp/test.mp4', start_time=2)

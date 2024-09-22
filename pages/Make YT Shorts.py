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
Generate_button = st.button('Generate YT Short')

if Generate_button:
    Short_Story = dna_gpt(f"Tell a shocking fact short story in 120 words about: {Short_Title}. Start with the words Did you know that")

    st.text_area(label="Short Story", value=Short_Story)

    asyncio.run(tts(Short_Story))
    st.audio(".temp/test.mp3")

    Prompt = dna_gpt(f"Make a good promt (max 70 tokens) for drawing fotorealistic HD 4K with epic detailed background, medieval: {Short_Title}")
    imagesURLs = asyncio.run(txt2img_shorts(RUNWARE_API_KEY, Prompt))
    st.image(imagesURLs)
    

    audio_clip = AudioFileClip(f".temp/test.mp3").volumex(1.2)

    bg_audio_clip = AudioFileClip(f".temp/bgm.MP3").volumex(1)

    final_audio_clip = CompositeAudioClip([audio_clip, bg_audio_clip.set_duration(audio_clip.duration)])

    imgs = [Image.open(requests.get(iu, stream=True).raw) for iu in imagesURLs]
    pil_imgs_im = [ImageClip(np.array(im)).set_duration(audio_clip.duration / len(imgs)) for im in imgs]
    final_clip = concatenate_videoclips(pil_imgs_im, method='compose').set_audio(final_audio_clip)
    final_clip.write_videofile(f'.temp/test.mp4', fps=3)

    st.video('.temp/test.mp4')

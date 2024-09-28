
import streamlit as st
from st_app_lib import *
import asyncio
from time import sleep

imagesURLs = asyncio.run(t2i(RUNWARE_API_KEY, "Thor, the mighty god of Asgard", height=512, width=512, numberResults=1))
image_path = imagesURLs[0]
st.image(image_path)
print(image_path)
ups_imgs = asyncio.run(upscaler(RUNWARE_API_KEY, image_path, 4))
print(ups_imgs[0].imageURL)
st.image(ups_imgs[0].imageURL)
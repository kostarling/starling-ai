
import streamlit as st
from st_app_lib import *
import asyncio
from time import sleep

imagesURLs = asyncio.run(t2i(RUNWARE_API_KEY, "Thor, the mighty god of Asgard", height=512, width=512, numberResults=5))
st.image(imagesURLs)
sleep(20)
imagesURLs1 = imagesURLs + asyncio.run(t2i(RUNWARE_API_KEY, "Thor, the mighty god of Asgard", height=512, width=512, numberResults=5))
st.image(imagesURLs1)
sleep(20)
imagesURLs2 = imagesURLs1 + asyncio.run(t2i(RUNWARE_API_KEY, "Thor, the mighty god of Asgard", height=512, width=512, numberResults=5))
st.image(imagesURLs2)

from super_image import EdsrModel, ImageLoader
from PIL import Image
import requests


image = Image.open(requests.get(imagesURLs[0], stream=True).raw)

model = EdsrModel.from_pretrained('eugenesiow/edsr-base', scale=2)
inputs = ImageLoader.load_image(image)
preds = model(inputs)

ImageLoader.save_image(preds, '.temp/scaled_2x.png')
ImageLoader.save_compare(inputs, preds, '.temp/scaled_2x_compare.png')

st.image('.temp/scaled_2x.png')
st.image('.temp/scaled_2x_compare.png')
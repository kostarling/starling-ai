from runware import Runware, IImageInference
import streamlit as st

RUNWARE_API_KEY = st.secrets["RUNWARE_API_KEY"]

async def txt2img(RUNWARE_API_KEY, Prompt):
    runware = Runware(api_key=RUNWARE_API_KEY)
    await runware.connect()

    request_image = IImageInference(
    positivePrompt=Prompt,
    model="runware:100@1",
    numberResults=1,
    negativePrompt="cloudy, rainy",
    useCache=False,
    height=768,
    width=512,
    )

    images = await runware.imageInference(requestImage=request_image)
    for image in images:
        print(f"Image URL: {image.imageURL}")
        #st.text(f"Image URL: {image.imageURL}")

        #st.image(image.imageURL)
    return image.imageURL

def dna_gpt(porompt):
  import requests
  response = requests.get(f"https://kostarling.pythonanywhere.com/info?data={porompt}")
  return response.text

import edge_tts
async def tts(TEXT) -> None:
    """Main function"""
    communicate = edge_tts.Communicate(text=TEXT, 
                                       voice="en-US-AndrewNeural",
                                       pitch="-20Hz",
                                       rate="+10%",
                                       volume="+5%")
    await communicate.save(".temp/test.mp3")


async def txt2img_shorts(RUNWARE_API_KEY, Prompt):
    runware = Runware(api_key=RUNWARE_API_KEY)
    await runware.connect()

    request_image = IImageInference(
    positivePrompt=Prompt,
    model="runware:100@1",
    numberResults=5,
    negativePrompt="cloudy, rainy",
    useCache=False,
    height=768,
    width=512,
    )

    images = await runware.imageInference(requestImage=request_image)

    imageURLs = [image.imageURL for image in images]

    return imageURLs
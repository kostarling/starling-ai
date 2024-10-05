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
    height=1280,
    width=768,
    )

    images = await runware.imageInference(requestImage=request_image)

    imageURLs = [image.imageURL for image in images]

    return imageURLs

import numpy as np
import cv2
def Zoom(clip,mode='in',position='center',speed=1):
    fps = clip.fps
    duration = clip.duration
    total_frames = int(duration*fps)
    def main(getframe,t):
        frame = getframe(t)
        h,w = frame.shape[:2]
        i = t*fps
        if mode == 'out':
            i = total_frames-i
        zoom = 1+(i*((0.1*speed)/total_frames))
        positions = {'center':[(w-(w*zoom))/2,(h-(h*zoom))/2],
                     'left':[0,(h-(h*zoom))/2],
                     'right':[(w-(w*zoom)),(h-(h*zoom))/2],
                     'top':[(w-(w*zoom))/2,0],
                     'topleft':[0,0],
                     'topright':[(w-(w*zoom)),0],
                     #'bottom':[(w-(w*zoom))/2,(h-(h*zoom))],
                     #'bottomleft':[0,(h-(h*zoom))],
                     'bottomright':[(w-(w*zoom)),(h-(h*zoom))]
                     }
        tx,ty = positions[position]
        M = np.array([[zoom,0,tx], [0,zoom,ty]])
        frame = cv2.warpAffine(frame,M,(w,h))
        return frame
    return clip.fl(main)


async def t2i(RUNWARE_API_KEY, Prompt,height, width, numberResults):
    runware = Runware(api_key=RUNWARE_API_KEY)
    await runware.connect()

    request_image = IImageInference(
    positivePrompt=Prompt,
    model="runware:100@1",
    numberResults=numberResults,
    negativePrompt="cloudy, rainy",
    useCache=False,
    height=height,
    width=width,
    )

    images = await runware.imageInference(requestImage=request_image)

    imageURLs = [image.imageURL for image in images]

    return imageURLs

def gpt4o(prompt):
    from g4f.client import Client

    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", 
                "content": prompt}]
    )

    return response.choices[0].message.content


from runware import Runware, IImageUpscale
async def upscaler(RUNWARE_API_KEY, image_path, upscale_factor) -> None:
    runware = Runware(api_key=RUNWARE_API_KEY)
    await runware.connect()

    upscale_gan_payload = IImageUpscale(
    inputImage=image_path, upscaleFactor=upscale_factor
    )
    upscaled_images = await runware.imageUpscale(upscaleGanPayload=upscale_gan_payload)
    
    return upscaled_images

async def i2i(RUNWARE_API_KEY, Prompt, height, width, numberResults, ):
    runware = Runware(api_key=RUNWARE_API_KEY)
    await runware.connect()

    request_image = IImageInference(
    positivePrompt=Prompt,
    model="runware:100@1",
    numberResults=numberResults,
    negativePrompt="cloudy, rainy",
    useCache=False,
    height=height,
    width=width,
    )

    images = await runware.imageInference(requestImage=request_image)

    imageURLs = [image.imageURL for image in images]

    return imageURLs
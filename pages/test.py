import streamlit as st
import asyncio
from runware import Runware, IImageInference

async def main():
    runware = Runware(api_key=st.secrets["RUNWARE_API_KEY"])
    await runware.connect()

    request_image = IImageInference(
    positivePrompt="Write beautiful text Book Cover",
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

# Синхронный вызов асинхронной функции через asyncio.run()
if st.button('Запустить асинхронную функцию'):
    result = asyncio.run(main())
    st.image(result)
    st.write(result)
from st_app_lib import *
from st_app_lib import *
import asyncio

RUNWARE_API_KEY = st.secrets["RUNWARE_API_KEY"]

prompt = st.text_input("Tshirt prompt", "Anime girl")

p_imare = asyncio.run(t2i(RUNWARE_API_KEY, prompt, 512, 512, 1))

br_imare = asyncio.run(br(p_imare[0]))

#st.image(p_imare)
#st.image(br_imare)

from PIL import Image
import requests

my_url = "https://im.runware.ai/image/ws/0.5/ii/a4f85127-5b7c-4c98-96c8-41364a86c88a.png"
im1 = Image.open("/workspaces/starling-ai/tshirt.jpg")


img = Image.open(requests.get(br_imare, stream=True).raw)
img = img.convert("RGBA")

datas = img.getdata()

newData = []

for item in datas:
		if item[0] == 255 and item[1] == 255 and item[2] == 255:
			newData.append((255, 255, 255, 0))
		else:
			newData.append(item)

img.putdata(newData)

im1.paste(img.resize([175,175]), (90, 130), img.resize([175,175]))

tsirt_col, image_col = st.columns(2)

tsirt_col.image(im1)
image_col.image(img)

# Create a download button
import io
buffer = io.BytesIO()
img.save(buffer, format="PNG")
byte_image = buffer.getvalue()

image_col.download_button(
    label="Download pill image",
    data=byte_image,
    file_name=f"{prompt}.png",
    mime="image/png"
)
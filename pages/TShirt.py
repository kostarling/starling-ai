from st_app_lib import *
from st_app_lib import *
import asyncio

RUNWARE_API_KEY = st.secrets["RUNWARE_API_KEY"]

st.text_input("Tshirt prompt", "Dragon")

p_imare = asyncio.run(t2i(RUNWARE_API_KEY, "Prompt",512, 512, 1))

st.image(p_imare)

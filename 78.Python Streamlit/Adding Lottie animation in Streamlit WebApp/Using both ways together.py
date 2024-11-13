import json
import requests

import streamlit as st
from streamlit_lottie import st_lottie


# Directly via URL
url = requests.get("https://assets5.lottiefiles.com/packages/lf20_awP420Zf8l.json")
url_json = dict()
if url.status_code == 200:
	url_json = url.json()
else:
	print("Error in URL")

	# By Downloading and importing path
path = "D:\\Python Projects\\Streamlit_Lottie\\car\\lottie_car.json"
with open(path,"r") as file:
	url = json.load(file)



st.title("Adding Lottie Animation in Streamlit WebApp")

# Adding Car Animation (Downloaded JSON)
st_lottie(url,
	reverse=True,
	height=400,
	width=400,
	speed=1,
	loop=True,
	quality='high',
	key='Car'
)

# Adding Boy Animation (Dirctly URL)
st_lottie(url_json,
	height=400,
	width=400,
	speed=1,
	loop=True,
	quality='high',
	key='Boy'
)

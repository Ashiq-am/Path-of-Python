import json
import requests

import streamlit as st
from streamlit_lottie import st_lottie


url = requests.get(
	"https://assets2.lottiefiles.com/packages/lf20_mDnmhAgZkb.json")
url_json = dict()
if url.status_code == 200:
	url_json = url.json()
else:
	print("Error in URL")


st.title("Adding Lottie Animation in Streamlit WebApp")

st_lottie(url_json,
		# change the direction of our animation
		reverse=True,
		# height and width of animation
		height=400,
		width=400,
		# speed of animation
		speed=1,
		# means the animation will run forever like a gif, and not as a still image
		loop=True,
		# quality of elements used in the animation, other values are "low" and "medium"
		quality='high',
		# THis is just to uniquely identify the animation
		key='Car'
		)

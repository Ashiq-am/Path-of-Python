import json
import requests

import streamlit as st
from streamlit_lottie import st_lottie

url = requests.get(
	"https://assets2.lottiefiles.com/packages/lf20_mDnmhAgZkb.json")
# Creating a blank dictionary to store JSON file,
# as their structure is similar to Python Dictionary
url_json = dict()

if url.status_code == 200:
	url_json = url.json()
else:
	print("Error in the URL")


st.title("Adding Lottie Animation in Streamlit WebApp")

st_lottie(url_json)

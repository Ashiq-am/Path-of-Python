import streamlit as stm
from streamlit_extras.keyboard_url import keyboard_to_url
from streamlit_extras.keyboard_text import key

keyboard_to_url(key="G", url="https://www.geeksforgeeks.org/")
stm.write(
	f"""Now hit {key("G", False)} on your keyboard...!""",
	unsafe_allow_html=True,
)

# keeping it True after G will print G on screen, False will not show

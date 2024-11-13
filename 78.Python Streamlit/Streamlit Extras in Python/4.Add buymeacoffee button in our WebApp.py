import streamlit as stm
from streamlit_extras.buy_me_a_coffee import button

stm.set_page_config(page_title = "This is a Simple Streamlit WebApp")
stm.title("This is the Home Page Geeks.")
stm.text("Geeks Home Page")

button(username="Geeks", floating=False, width=250)

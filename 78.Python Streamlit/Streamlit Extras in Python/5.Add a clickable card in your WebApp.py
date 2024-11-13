import streamlit as stm
from streamlit_card import card


stm.set_page_config(page_title="This is a Simple Streamlit WebApp")
stm.title("This is the Home Page Geeks.")
stm.text("Geeks Home Page")


# Card

card(
	title="Hello Geeks!",
	text="Click this card to redirect to GeeksforGeeks",
	image="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190710102234/download3.png",
	url="https://www.geeksforgeeks.org/",
)

import streamlit as stm
from streamlit_extras import add_vertical_space as avs

stm.set_page_config(page_title="This is a Simple Streamlit WebApp")
stm.title("This is the Home Page Geeks.")
stm.text("Geeks Home Page")

# Text before putting space
stm.write("The text after which we will put spaces")

# Putting 5 vertical spaces
avs.add_vertical_space(5)

# Text after the 5th space.
stm.write("The text after putting spaces")

import streamlit as stm
from streamlit_extras import add_vertical_space as avs
import annotated_text as ant
from annotated_text import annotation

stm.set_page_config(page_title="This is a Simple Streamlit WebApp")
stm.title("This is the Home Page Geeks.")
stm.text("Geeks Home Page")

# Vertical Space
stm.write("The text after which we will put spaces")
avs.add_vertical_space(5)
stm.write("The text after putting spaces")

# Annotated Text
ant.annotated_text(
    "Hey",
    annotation("GeeksforGeeks", color='#07a631'),
    ("is", "the", 'blue'),

    # Text is - 'is','the',
    # the color of them is 'blue',
    # we don't need to use color
    # kwarg here like annotation
    # function below to give color.
    # We can also provide Hex values of colors as well as names
    annotation("BEST", border='3px groove yellow'),
    annotation("for", "EVERYTHING", color='#f7f8fa')
)

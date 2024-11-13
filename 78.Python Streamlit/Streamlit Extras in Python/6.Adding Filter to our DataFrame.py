import streamlit as stm
from streamlit_extras.dataframe_explorer import dataframe_explorer
import pandas as pd


stm.set_page_config(page_title="This is a Simple Streamlit WebApp")
stm.title("This is the Home Page Geeks.")
stm.text("Geeks Home Page")


df = pd.read_csv('iris.csv')

filtered_df = dataframe_explorer(df)
stm.dataframe(filtered_df, use_container_width=True)

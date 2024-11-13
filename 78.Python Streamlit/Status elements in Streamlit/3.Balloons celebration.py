import streamlit as st
import pandas as pd

df = pd.read_csv("iris.csv")

col = st.sidebar.multiselect("Select any column",
							df.columns)

st.balloons()

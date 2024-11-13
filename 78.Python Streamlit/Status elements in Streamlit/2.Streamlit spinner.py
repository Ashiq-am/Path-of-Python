import streamlit as st
import pandas as pd
import time

df = pd.read_csv("iris.csv")

col = st.sidebar.multiselect("Select any column",
							df.columns)

with st.spinner("Just a moment ..."):
	time.sleep(1)
st.success('Done!')
st.dataframe(df[col])

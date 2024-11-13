# Python3 program to illustrate
# How to make an area chart
# using the altair library

# Importing altair and vega_datasets
import altair as alt
from vega_datasets import data

# Selecting the sp500 dataset
sp500 = data.sp500()

# Making the area graph
# using the mark_area function
alt.Chart(sp500).mark_area().encode(

    # Map the date to x-axis
    x='date',

    # Map the price to y-axis
    y='price'
)

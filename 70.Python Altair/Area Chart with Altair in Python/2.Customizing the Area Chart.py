# Python3 program to illustrate
# How to make an area chart
# using the altair library

# Importing altair and vega_datasets
import altair as alt
from vega_datasets import data

# Selecting the sp500 dataset
sp500 = data.sp500()

# Making the area graph
alt.Chart(sp500).mark_area(color='green',
                           opacity=0.5,
                           line={'color': 'darkgreen'}).encode(

    # Map the date to x-axis
    x='date',

    # Map the price to y-axis
    y='price'
)

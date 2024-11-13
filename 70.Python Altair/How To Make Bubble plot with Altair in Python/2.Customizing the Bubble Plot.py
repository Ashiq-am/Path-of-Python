# Python3 program to illustrate
# how to customize a bubble plot

# Importing altair and vega_datasets
import altair as alt
from vega_datasets import data

# Selecting the cars dataset
cars = data.cars()

# Making the base scatter plot
# and adding the customizations
alt.Chart(cars).mark_point(color='green',
                           filled=True,
                           opacity=0.4).encode(

    # Map the sepalLength to x-axis
    x='Acceleration',

    # Map the petalLength to y-axis
    y='Displacement',

    # Map the Cylinders variable to size
    # and specify it as a nominal variable
    size='Cylinders:N'
)

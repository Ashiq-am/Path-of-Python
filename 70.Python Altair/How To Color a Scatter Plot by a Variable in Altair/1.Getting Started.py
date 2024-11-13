# Python3 program to illustrate
# How to color a Scatter Plot
# using altair

# Importing altair and vega_datasets library
import altair as alt
from vega_datasets import data

# Selecting the iris dataset
iris = data.iris()

# Making the Scatter Plot
alt.Chart(iris).mark_point().encode(
# Map the sepalLength to x-axis
	x = 'sepalLength',
# Map the petalLength to y-axis
	y = 'petalLength',
)

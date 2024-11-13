# Importing altair
import altair as alt
# Import data object from vega_datasets
from vega_datasets import data

# Selecting the data
iris = data.iris()

# Making the Scatter Plot
alt.Chart(iris).mark_point().encode(
	# Map the sepalLength to x-axis
	x='sepalLength',
	# Map the petalLength to y-axis
	y='petalLength',
	# Map the species to shape
	shape='species'
)

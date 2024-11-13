# import libraries
import altair as alt
from vega_datasets import data

# load data
cars = data.cars()

# Draw Facet Scatter Plot
alt.Chart(cars).mark_point().encode(
	x = alt.X('Displacement'),
	y = alt.Y('Acceleration'),
	size = alt.value(100),
	color = 'Cylinders'
).properties(width = 250, height = 250).facet(
	'Origin:N',
	columns = 3
)

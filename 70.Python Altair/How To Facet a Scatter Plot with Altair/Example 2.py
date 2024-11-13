# import libraries
import altair as alt
from vega_datasets import data

# load data
iris = data.iris()

# Draw Facet Scatter Plot
alt.Chart(iris).mark_point().encode(
	x = alt.X('sepalLength'),
	y = alt.Y('sepalWidth'),
	color = 'species'
).properties(width = 250, height = 250).facet(
	'species:N',
	columns = 3
)

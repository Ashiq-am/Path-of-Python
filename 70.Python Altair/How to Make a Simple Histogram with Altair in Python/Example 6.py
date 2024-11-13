# importing libraries
import altair as alt
from vega_datasets import data

# importing cars dataset
# form vega_datasets provided by altair
iris_data = data.iris()

# making the simple histogram
# on sepal length by setting bin
# and color on the basis of species
hist = alt.Chart(iris_data).mark_bar().encode(x = alt.X('sepalLength',
														bin = alt.BinParams(maxbins = 20)),
											y = 'count()',color = 'species')
# showing the histogram
hist.show()

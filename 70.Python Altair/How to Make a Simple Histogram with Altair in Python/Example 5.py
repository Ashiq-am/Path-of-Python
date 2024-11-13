# importing libraries
import altair as alt
from vega_datasets import data

# importing cars dataset
# form vega_datasets provided by altair
iris_data = data.iris()

# making the simple histogram on sepal length
hist = alt.Chart(iris_data).mark_bar().encode(x = 'sepalLength',
											y = 'count()')

# showing the histogram
hist.show()

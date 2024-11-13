# importing libraries
import altair as alt
from vega_datasets import data

# importing cars dataset
# form vega_datasets provided by altair
car_data = data.cars()

# making the simple histogram
# on Horsepower by setting the bin
hist = alt.Chart(car_data).mark_bar().encode(x = alt.X('Horsepower',
													bin = alt.BinParams(maxbins = 20)),
											y = 'count()')
# showing the histogram
hist.show()

# importing libraries
import altair as alt
from vega_datasets import data

# importing cars dataset
# form vega_datasets provided by altair
car_data = data.cars()

# making the simple histogram
# on Acceleration by setting the bin
hist = alt.Chart(car_data).mark_bar().encode(x = alt.X('Acceleration',
													bin = alt.BinParams(maxbins = 30)),
											y = 'count()')
# showing the histogram
hist.show()

# importing libraries
import altair as alt
from vega_datasets import data
import vega_datasets

# importing cars dataset form
# vega_datasets provided by altair
car_data = data.cars()

# printing the dataset
display(car_data)

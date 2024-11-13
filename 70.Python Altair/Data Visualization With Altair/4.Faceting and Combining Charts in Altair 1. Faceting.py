import altair as alt
from vega_datasets import data

# Load the dataset
cars = data.cars()
facet_chart = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin'
).facet(
    column='Origin'
)

facet_chart

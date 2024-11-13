import altair as alt
from vega_datasets import data

cars = data.cars()

# Create the Altair chart
chart = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Cylinders:O'
).facet(
    column='Origin'
).resolve_scale(
    y='shared'
)

chart

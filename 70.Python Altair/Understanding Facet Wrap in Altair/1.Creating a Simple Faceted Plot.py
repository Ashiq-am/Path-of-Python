import altair as alt
from vega_datasets import data

iris = data.iris()

# Facet by species into rows
chart_row = alt.Chart(iris).mark_point().encode(
    x='petalLength:Q',
    y='petalWidth:Q',
    color='species:N'
).facet(
    row='species:N'
)

# Facet by species into columns
chart_column = alt.Chart(iris).mark_point().encode(
    x='petalLength:Q',
    y='petalWidth:Q',
    color='species:N'
).facet(
    column='species:N'
)
chart

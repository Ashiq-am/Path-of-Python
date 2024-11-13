import altair as alt
from vega_datasets import data

source = data.population.url

# Create a faceted chart with multiple columns
chart = alt.Chart(source).mark_area().encode(
    x='age:O',
    y=alt.Y('sum(people):Q', title='Population'),
    facet=alt.Facet('year:O', columns=5)  # Specify number of columns
).properties(
    width=200,
    height=80
)
chart

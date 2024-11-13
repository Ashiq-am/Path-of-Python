import altair as alt
from vega_datasets import data

source = data.cars.url

# Create a chart with a title and subtitle
chart = alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q'
).properties(
    title=alt.TitleParams(
        text='Cars Data',
        subtitle='Analysis of Horsepower vs. Miles per Gallon'
    )
)

chart

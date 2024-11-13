import altair as alt
from vega_datasets import data

source = data.cars.url

# Main chart
main_chart = alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q'
)

# Subtitle as a separate text mark
subtitle = alt.Chart().mark_text(
    align='center',
    baseline='top',
    dx=0,
    dy=20  # Adjust position as needed
).encode(
    text=alt.value('Analysis of Horsepower vs. Miles per Gallon')
).properties(
    width=400,
    height=30
)

# Concatenate the main chart and subtitle
chart_with_subtitle = alt.vconcat(subtitle, main_chart)

chart_with_subtitle

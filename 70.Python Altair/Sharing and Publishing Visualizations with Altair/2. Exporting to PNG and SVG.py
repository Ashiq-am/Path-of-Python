import altair as alt
from vega_datasets import data
import vl_convert as vlc

# Create an Altair chart
chart = alt.Chart(data.cars.url).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color='Origin:N'
)

chart_json = chart.to_json()

# Save the chart as SVG
svg_str = vlc.vegalite_to_svg(chart_json)
with open("chart.svg", "w") as f:
    f.write(svg_str)

# Save the chart as PNG
png_data = vlc.vegalite_to_png(chart_json)
with open("chart.png", "wb") as f:
    f.write(png_data)

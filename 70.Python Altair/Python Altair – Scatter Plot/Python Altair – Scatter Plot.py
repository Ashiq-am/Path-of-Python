# import required modules
import altair as alt
from vega_datasets import data


# assign dataset
seattle_weather = data.seattle_weather()

# display dataset
seattle_weather.head(5)

# depict scatter plot
alt.Chart(seattle_weather).mark_point().encode(
	x='temp_max',
	y='temp_min'
)

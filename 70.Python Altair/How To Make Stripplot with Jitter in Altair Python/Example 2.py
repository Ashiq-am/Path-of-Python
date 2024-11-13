#import libraries
import altair as alt
from vega_datasets import data

# Getting data
weather = data.seattle_weather()

# plotting the stripplot
stripplot = alt.Chart(weather).mark_circle(size=14).encode(
	x=alt.X(
		'jitter:Q',
		title=None,
		axis=alt.Axis(ticks=True, grid=False, labels=False),
		scale=alt.Scale(),
	),
	y=alt.Y('temp_max:Q',
			scale=alt.Scale(
				domain=(-1, 40))),
	color=alt.Color('weather:N', legend=None),
	column=alt.Column(
		'weather:N',
		header=alt.Header(
			labelFontSize=16,
			labelAngle=0,
			titleOrient='top',
			labelOrient='bottom',
			labelAlign='center',
			labelPadding=25,
		),
	),
).transform_calculate(
	# Generate Gaussian jitter with a Box-Muller transform
	jitter='sqrt(-2*log(random()))*cos(2*PI*random())'
).configure_facet(
	spacing=0
).configure_view(
	stroke=None
).configure_axis(
	labelFontSize=16,
	titleFontSize=16
).properties(height=400, width=100)
stripplot

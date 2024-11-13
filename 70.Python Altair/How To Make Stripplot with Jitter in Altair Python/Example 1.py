#import libraries
import seaborn
import altair as alt


# Getting data
tip = seaborn.load_dataset('tips')

# plotting the stripplot
stripplot = alt.Chart(tip).mark_circle(size=14).encode(
	# X-axis jitter Vertical
	x=alt.X(
		'jitter:Q',
		title=None,
		axis=alt.Axis(ticks=True, grid=False, labels=False),
		scale=alt.Scale(),
	),
	y=alt.Y('tip:Q',
			scale=alt.Scale()),
	color=alt.Color('time:N', legend=None),
	column=alt.Column(
		'time:N',
	),
).transform_calculate(
	# Generate Gaussian jitter with a Box-Muller transform
	jitter='sqrt(-2*log(random()))*cos(2*PI*random())')
stripplot

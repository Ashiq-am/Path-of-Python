#import libraries
import seaborn
import altair as alt
import pandas as pd

# Creating our own data
data = [['Tom', 10, 'Male'], ['Nick', 25, 'Male'], ['Juli', 14, 'Female'],
		['Sarah', 30, 'Male'], ['Pulkit', 20, 'Male'], ['Ritika', 20, 'Female'],
		['Sayantan', 60, 'Male'], ['Pam', 39, 'Female'], ['Peter', 42, 'Male'],
		['Jenefer', 24, 'Female'], ['Tony', 29, 'Female'], ['Myler', 22, 'Female']]
df = pd.DataFrame(data, columns=['Name', 'Age', 'Gender'])

# plotting the stripplot Horizontal
horizontal_stripplot = alt.Chart(df, width=600, height=100).mark_circle(size=40).encode(
	y=alt.Y(
		'jitter:Q',
		title=None,
		axis=alt.Axis(ticks=True, grid=False, labels=False),
		scale=alt.Scale(),
	),
	x=alt.X('Age:Q', scale=alt.Scale()),
	color=alt.Color('Gender:N', legend=None),
	row=alt.Row(
		'Gender:N',
		header=alt.Header(
			labelAngle=0,
			labelFontSize=16,
			titleOrient='top',
			labelOrient='left',
			labelAlign='left',
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
)
horizontal_stripplot

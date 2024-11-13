import pandas as pd
import numpy as np
import plotly.express as px
import string
import plotly.graph_objects as go

# create a dataframe
cols = ['a', 'b', 'c', 'd', 'e']
n = 50

df = pd.DataFrame({'Date': pd.date_range('2021-1-1', periods=n)})

# create data with vastly different ranges
for col in cols:
	start = np.random.choice([1, 10, 100, 1000, 100000])
	s = np.random.normal(loc=0, scale=0.01*start, size=n)
	df[col] = start + s.cumsum()

# melt data columns from wide to long
dfm = df.melt("Date")

# make the plot
fig = px.line(
	data_frame=dfm,
	x='Date',
	y='value',
	facet_col='variable',
	facet_col_wrap=6,

	height=500,
	width=1000,
	title='Geeksforgeeks',
	labels={
		'Date': 'Date',
		'value': 'Value',
		'variable': 'Plot no.'
	}
)

# hide subplot y-axis titles and x-axis titles
for axis in fig.layout:
	if type(fig.layout[axis]) == go.layout.YAxis:
		fig.layout[axis].title.text = ''
	if type(fig.layout[axis]) == go.layout.XAxis:
		fig.layout[axis].title.text = ''

# ensure that each chart has its own y rage and tick labels
fig.update_yaxes(matches=None, showticklabels=True, visible=True)

fig.show()

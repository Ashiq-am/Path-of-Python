from plotly import tools
import plotly.graph_objs as go
from plotly.offline import iplot
import numpy as np

# defining data for chart 1
x1 = np.array([22, 87, 5, 43, 56, 73, 11,
			42, 20, 5, 31, 27, 85])

# defining data for chart 2
N = 100
x_vals = np.linspace(0, 1, N)
y_vals = np.random.randn(N) - 5

# chart 1
chart1 = go.Histogram(x=x1)

# chart 2
chart2 = go.Scatter(
	x=x_vals,
	y=y_vals,
	mode='lines',
	name='line',
	xaxis='x2',
	yaxis='y2',
)

data = [chart1, chart2]

# setting layout
layout = go.Layout(

	# setting y-axis position for chart 2
	xaxis2=dict(
		domain=[0.65, 0.95],
		anchor='y2'
	),

	# setting y-axis position for chart 2
	yaxis2=dict(
		domain=[0.6, 0.95],
		anchor='x2'
	)
)

fig = go.Figure(data=data, layout=layout)
iplot(fig)

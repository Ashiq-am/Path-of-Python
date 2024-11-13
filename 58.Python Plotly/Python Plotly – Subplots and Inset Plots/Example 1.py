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
fig = tools.make_subplots(rows=1, cols=2)
fig.append_trace(chart1, 1, 1)
fig.append_trace(chart2, 1, 2)
fig['layout'].update(height=600, width=800,
					title='subplot')
iplot(fig)

import plotly.express as px
import plotly.graph_objects as go
import numpy as np

X = np.linspace(-1, 1, 100)
Y = np.sinc(X)

x = [-0.89, -0.24, -0.0, 0.41, 0.89, ]
y = [0.36, 0.75, 1.03, 0.65, 0.28, ]

fig = go.Figure()
fig.add_trace(go.Scatter(
	x=X, y=Y,
	name='error bar'
))

fig.add_trace(go.Scatter(
	x=x, y=y,
	mode='markers',
	name='measured',
	error_y=dict(
		type='constant',
		value=0.1,
		color='green',
		thickness=1.5,
		width=3,
	),
	error_x=dict(
		type='constant',
		value=0.2,
		color='blue',
		thickness=1.5,
		width=3,
	),
	marker=dict(color='green', size=8)
))

fig.show()

import plotly.graph_objects as go
import numpy as np

fig = go.Figure(data=go.Line(
	y = np.random.randn(500),
	mode='markers',
	marker=dict(
		size=8,
		color=np.random.randn(500), #set color equal to a variable
		colorscale='hot_r', # one of plotly colorscales
		showscale=True # enable color scale
	)
))

fig.show()

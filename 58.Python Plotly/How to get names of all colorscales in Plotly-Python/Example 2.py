import plotly.graph_objects as go
import numpy as np

fig = go.Figure(data=go.Scatter(
	y=np.random.randn(500),
	mode='markers',
	marker=dict(
		size=8,
		color=np.random.randn(550), # set color equal to a variable
		colorscale='Agsunset_r', # reverse Agsunset colorscales
		showscale=True
	)
))

fig.update_layout(
	margin=dict(l=12, r=5, t=20, b=20),
	paper_bgcolor="LightSteelBlue",
)


fig.show()

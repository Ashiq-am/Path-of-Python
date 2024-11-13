import plotly.graph_objects as go
import plotly.express as px
import numpy as np

df = px.data.tips()

x1 = np.linspace(-4, 4, 9)
y1 = np.linspace(-5, 5, 11)
z1 = np.linspace(-5, 5, 11)

X, Y, Z = np.meshgrid(x1, y1, z1)

values = (np.sin(X**2 + Y**2))/(X**2 + Y**2)

fig = go.Figure(data=go.Volume(
	x=X.flatten(),
	y=Y.flatten(),
	z=Z.flatten(),
	isomin=-0.5,
	isomax=0.5,
	value=values.flatten(),
	opacity=0.1,
	opacityscale=[[-0.5, 1], [-0.2, 0], [0.2, 0], [0.5, 1]],
	colorscale='RdBu'
	))

fig.show()

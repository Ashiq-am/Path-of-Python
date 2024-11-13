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
	value=values.flatten(),
	opacity=0.1,
	caps= dict(x_show=False, y_show=True, z_show=False),
	))
fig.show()

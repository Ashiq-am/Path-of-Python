import plotly.graph_objects as go
import numpy as np

x, y, z = np.mgrid[0:20, 0:20, 0:20]
x = x.flatten()
y = y.flatten()
z = z.flatten()

u = np.zeros_like(x)
v = np.zeros_like(y)
w = z**2

fig = go.Figure(data=go.Streamtube(x=x, y=y, z=z, u=u, v=v, w=w))
fig.show()

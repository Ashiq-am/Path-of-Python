import plotly.graph_objects as go
import numpy as np


x = np.linspace(1, 15, 20)
y = np.linspace(10, 15, 20)

fig = go.Figure()

fig.add_trace(go.Scatter(
	x=x,
	y=y
))

fig.update_layout(xaxis_type="log")
fig.show()

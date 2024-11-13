import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np

x = np.linspace(-2, 2, 60)
y = np.linspace(-1, 1, 60)
Y, X = np.meshgrid(x, y)
u = np.cos(X)*Y
v = np.sin(X)*Y

# Create quiver plot
fig = ff.create_quiver(x, y, u, v, arrow_scale=.1)

# Adding scatter as the origin
fig.add_trace(go.Scatter(x = [0], y = [0],
						mode = 'markers',
						marker_size = 15
						))

fig.show()

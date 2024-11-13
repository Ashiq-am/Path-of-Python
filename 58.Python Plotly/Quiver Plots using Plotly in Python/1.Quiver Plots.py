import plotly.figure_factory as ff
import numpy as np

x = np.linspace(-2, 2, 60)
y = np.linspace(-1, 1, 60)
Y, X = np.meshgrid(x, y)
u = 1 - X**2 + Y
v = -1 + X - Y**2

# Create quiver plot
fig = ff.create_quiver(x, y, u, v, arrow_scale=.1)

fig.show()

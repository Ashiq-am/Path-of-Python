from plotly.figure_factory import create_2d_density
import numpy as np


# Make data points
t = np.linspace(-1,1.2,2000)
x = (t**3)+(0.3*np.random.randn(2000))
y = (t**6)+(0.3*np.random.randn(2000))

# Create custom colorscale
colorscale = ['#7A4579', '#D56073', 'rgb(236,158,105)',
			(1, 1, 0.2), (0.98,0.98,0.98)]

# Create a figure
fig = create_2d_density(x, y, colorscale=colorscale,
	hist_color='rgb(255, 237, 222)', point_size=3)

# Plot the data
fig.show()

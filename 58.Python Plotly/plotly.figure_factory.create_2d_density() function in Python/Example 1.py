from plotly.figure_factory import create_2d_density
import numpy as np


t = np.linspace(-1,1.2,2000)
x = (t**3)+(0.3*np.random.randn(2000))
y = (t**6)+(0.3*np.random.randn(2000))

fig = create_2d_density(x, y)
fig.show()

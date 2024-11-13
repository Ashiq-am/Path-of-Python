import plotly.graph_objects as px
import numpy as np

# creating random data through randomint
# function of numpy.random
np.random.seed(42)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

size = [20, 40, 60, 80, 100, 80, 60, 40, 20, 40]

plot = px.Figure(data=[px.Scatter(
    x=random_x,
    y=random_y,
    mode='markers',
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2. * max(size) / (40. ** 2),
        sizemin=4
    )
)])

plot.show()

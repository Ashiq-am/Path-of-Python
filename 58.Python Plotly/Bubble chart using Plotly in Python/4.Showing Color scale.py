import plotly.graph_objects as px
import numpy as np

# creating random data through randomint
# function of numpy.random
np.random.seed(42)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

plot = px.Figure(data=[px.Scatter(
    x=random_x,
    y=random_y,
    mode='markers',
    marker=dict(
        color=[10, 20, 30, 50],
        size=[10, 30, 50, 80],
        showscale=True
    )
)])

plot.show()

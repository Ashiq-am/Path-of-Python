import plotly.graph_objects as px
import numpy

# creating random data through randomint
# function of numpy.random
np.random.seed(42)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

x = ['A', 'B', 'C', 'D']

plot = px.Figure(data=[go.Bar(
    name='Data 1',
    x=x,
    y=[100, 200, 500, 673]
),
    go.Bar(
        name='Data 2',
        x=x,
        y=[56, 123, 982, 213]
    )
])

plot.show()

import plotly.graph_objects as go
import numpy

plot = go.Figure(data=[go.Scatter(
    x=np.random.randn(1000),
    y=np.random.randn(1000),
    stackgroup='one'),
    go.Scatter(
        x=np.random.randn(10),
        y=np.random.randn(50),
        stackgroup='one')
])

plot.show()

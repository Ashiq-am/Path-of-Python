import plotly.graph_objects as go
import plotly.express as px
import numpy

df = px.data.iris()

plot = go.Figure(data=[go.Scatter(
    x=df['sepal_width'],
    y=df['sepal_length'],
    stackgroup='one'),
    go.Scatter(
        x=df['petal_width'],
        y=df['petal_length'],
        stackgroup='one')
])

plot.show()

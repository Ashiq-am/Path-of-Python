import plotly.graph_objects as px
import plotly.express as go
import numpy as np

df = go.data.tips()

x = df['total_bill']
y = df['day']

plot = px.Figure(data=[px.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker_color='rgba(199, 10, 165, .9)')
])

plot.update_traces(mode='markers', marker_size=10)

plot.show()

import numpy as np
import plotly.graph_objects as go

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 3, 4, 5, 6]
fig = go.Figure(data=go.Scatter(x = x, y = y))
fig.show()

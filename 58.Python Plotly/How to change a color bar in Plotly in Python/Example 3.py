import plotly.graph_objects as go
import numpy as np

fig = go.Figure(data=go.Scatter(
    y=np.random.randn(500),
    mode='markers',
    marker=dict(
        size=8,

        # set color equal to a variable
        color=np.random.randn(550),

        # one of plotly colorscales
        colorscale='turbo_r',

        # enable color scale
        showscale=True
    )
))
# display
fig.show()

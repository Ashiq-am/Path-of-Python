# import the modules
import plotly.graph_objects as go
import numpy as np

# create figure
# from the data using numpy random method
fig = go.Figure(data=go.Scatter(
    y=np.random.randn(500),
    mode='markers',
    marker=dict(
        size=8,

        # set color equal to a variable
        color=np.random.randn(500),

        # one of plotly colorscales
        colorscale='hot',

        # enable color scale
        showscale=True
    )
))

# display figure
fig.show()

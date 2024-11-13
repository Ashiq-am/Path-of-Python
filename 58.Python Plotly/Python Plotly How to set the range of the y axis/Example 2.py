# Importing Libraries
import pandas as pd
import plotly.graph_objs as go
import numpy as np

np.random.seed(5)

# generating numbers ranging from 1 to 20
# on x-axis
x = list(range(1,20))

# generating random numbers on y-axis
y = np.random.randn(20)

# plotting scatter plot on x and y data with
# 'lines' as mode
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))

# setting the y-axis range from -3 to 3
fig.update_layout(yaxis_range=[-3,3])

# to display the figure in the output screen
fig.show()

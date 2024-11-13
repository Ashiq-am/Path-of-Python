# Importing Libraries
import pandas as pd
import plotly.graph_objs as go
import numpy as np

# generating numbers ranging from 1 to 20
# on x-axis
x = list(range(1,20))

# generating random numbers on y-axis
y = np.random.randn(20)

# plotting scatter plot on x and y data with 'lines'
# as mode and setting the y-axis range from -8 to 8
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'),
				layout_yaxis_range=[-8,8])

# to display the figure in the output screen
fig.show()

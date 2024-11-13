# importing required libraries
import numpy as np
import plotly
import chart_studio
import plotly.express as px

# assigning values to x and y
x = np.random.randint(low=1, high=50, size=50)
y = np.random.randint(low=51, high=100, size=50)

# creating and displaying graph
fig = px.scatter(x=x, y=y)
fig.show()

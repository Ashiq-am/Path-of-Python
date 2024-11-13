import plotly.express as px
import numpy as np

# Generate sample data
x = np.linspace(0, 100, 100)
y = np.sin(x)

# Create a scatter plot with a specified x-axis range
fig = px.scatter(x=x, y=y, range_x=[20, 80])
fig.show()

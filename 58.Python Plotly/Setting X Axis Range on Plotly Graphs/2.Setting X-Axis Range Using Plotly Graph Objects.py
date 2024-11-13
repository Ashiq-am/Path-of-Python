import plotly.graph_objects as go
import numpy as np

# Generate sample data
x = np.linspace(0, 100, 100)
y = np.sin(x)

# Create a scatter plot with a specified x-axis range
fig = go.Figure(go.Scatter(x=x, y=y))
fig.update_xaxes(range=[20, 80])
fig.show()

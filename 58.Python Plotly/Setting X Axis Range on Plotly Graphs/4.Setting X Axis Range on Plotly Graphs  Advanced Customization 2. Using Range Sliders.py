import plotly.graph_objects as go
import numpy as np

# Generate sample data
x = np.linspace(0, 100, 100)
y = np.sin(x)

# Create a scatter plot with a range slider
fig = go.Figure(go.Scatter(x=x, y=y))
fig.update_xaxes(rangeslider_visible=True)
fig.show()

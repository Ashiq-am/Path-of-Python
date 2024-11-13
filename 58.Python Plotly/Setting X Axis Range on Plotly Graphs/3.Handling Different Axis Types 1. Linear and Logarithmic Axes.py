import plotly.graph_objects as go
import numpy as np

# Generate sample data
x = np.linspace(1, 100, 100)
y = np.power(x, 2)

# Create a scatter plot with a logarithmic x-axis
fig = go.Figure(go.Scatter(x=x, y=y))
fig.update_xaxes(type="log", range=[np.log10(10), np.log10(100)])
fig.show()

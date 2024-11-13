import plotly.graph_objects as go
import numpy as np

# Generate sample data
t = np.linspace(0, 10, 100)
x = np.sin(t)
y = np.cos(t)

# Create figure
fig = go.Figure(
    data=[go.Scatter(x=x, y=y, mode='markers')],
    layout=go.Layout(
        xaxis=dict(range=[-1.5, 1.5]),
        yaxis=dict(range=[-1.5, 1.5]),
        title="Animated Scatter Plot",
        updatemenus=[dict(type="buttons", buttons=[dict(label="Play", method="animate", args=[None])])]
    ),
    frames=[go.Frame(data=[go.Scatter(x=x[:k], y=y[:k], mode='markers')]) for k in range(1, len(x))]
)

# Show the plot
fig.show()

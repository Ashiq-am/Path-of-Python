import plotly.graph_objects as go
import numpy as np

n = 10000
plot = go.Figure(data=[go.Scatter(
    x=np.random.randn(n),
    mode='markers',
    marker=dict(
        color=np.random.randn(n),
        colorscale='Viridis',
        showscale=True
    )
)
])

plot.show()

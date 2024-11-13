import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Create subplots
fig = make_subplots(rows=2, cols=2)

# Add traces
fig.add_trace(go.Scatter(y=[1, 3, 2], mode='lines'), row=1, col=1)
fig.add_trace(go.Scatter(y=[4, 1, 3], mode='lines'), row=1, col=2)
fig.add_trace(go.Scatter(y=[5, 6, 4], mode='lines'), row=2, col=1)
fig.add_trace(go.Scatter(y=[7, 8, 6], mode='lines'), row=2, col=2)

# Update layout for borders
fig.update_layout(
    xaxis=dict(showline=True, linewidth=2, linecolor='black', mirror=True),
    yaxis=dict(showline=True, linewidth=2, linecolor='black', mirror=True),
    xaxis2=dict(showline=True, linewidth=2, linecolor='black', mirror=True),
    yaxis2=dict(showline=True, linewidth=2, linecolor='black', mirror=True),
    xaxis3=dict(showline=True, linewidth=2, linecolor='black', mirror=True),
    yaxis3=dict(showline=True, linewidth=2, linecolor='black', mirror=True),
    xaxis4=dict(showline=True, linewidth=2, linecolor='black', mirror=True),
    yaxis4=dict(showline=True, linewidth=2, linecolor='black', mirror=True),
    annotations=[
        dict(text="Label 1", xref="paper", yref="paper", x=0.25, y=1.05, showarrow=False),
        dict(text="Label 2", xref="paper", yref="paper", x=0.75, y=1.05, showarrow=False),
        dict(text="Label 3", xref="paper", yref="paper", x=0.25, y=-0.1, showarrow=False),
        dict(text="Label 4", xref="paper", yref="paper", x=0.75, y=-0.1, showarrow=False)
    ]
)

# Link x-axes and y-axes for synchronized panning
fig.update_xaxes(matches='x')
fig.update_yaxes(matches='y')

fig.show()

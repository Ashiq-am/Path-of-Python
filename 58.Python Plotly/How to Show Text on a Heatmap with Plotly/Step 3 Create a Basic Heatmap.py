import plotly.graph_objects as go

# Create heatmap
fig = go.Figure(data=go.Heatmap(
    z=data,
    colorscale='Viridis'
))

# Show figure
fig.show()

import plotly.graph_objects as go

# Create a figure
fig = go.Figure()

fig.add_trace(go.Scatter(x=[1, 2, 3, 4, 5], y=[2, 1, 6, 4, 4], mode='markers'))

# Add text annotation
fig.add_annotation(
    x=2, y=1,
    text="Custom Text",
    showarrow=True,
    arrowhead=2
)

# Update layout to accommodate the text
fig.update_layout(
    title="Example with Annotations",
    xaxis_title="X Axis",
    yaxis_title="Y Axis"
)

fig.show()

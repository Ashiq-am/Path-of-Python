# Customize heatmap
fig = go.Figure(data=go.Heatmap(
    z=data,
    text=text,
    texttemplate="%{text}",
    colorscale='Viridis',
    hoverinfo='z'  # Show data value on hover
))

# Customize layout
fig.update_layout(
    title='Heatmap with Annotations',
    xaxis_nticks=36,
    yaxis_nticks=36
)

# Show figure
fig.show()

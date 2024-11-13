# Generate text annotations
text = np.round(data, 2).astype(str)

# Create heatmap with annotations
fig = go.Figure(data=go.Heatmap(
    z=data,
    text=text,
    texttemplate="%{text}",
    colorscale='Viridis'
))

# Show figure
fig.show()

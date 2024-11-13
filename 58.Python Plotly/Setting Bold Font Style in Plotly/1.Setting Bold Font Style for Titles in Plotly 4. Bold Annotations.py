import plotly.graph_objects as go

fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 5, 6])])
fig.add_annotation(
    x=2, y=5,
    text="Bold Annotation",
    font=dict(family='Arial Black', size=16, color='black')
)
fig.show()

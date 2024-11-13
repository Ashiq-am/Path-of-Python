import plotly.graph_objects as go

fig = go.Figure(data=[go.Bar(x=['A', 'B', 'C'], y=[1, 3, 2])])
fig.update_layout(
    title='Graphs',
    xaxis=dict(tickfont=dict(family='Arial Black', size=14)),
    yaxis=dict(tickfont=dict(family='Arial Black', size=14))
)
fig.show()

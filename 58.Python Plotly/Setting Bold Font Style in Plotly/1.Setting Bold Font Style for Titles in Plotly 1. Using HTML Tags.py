import plotly.graph_objects as go

fig = go.Figure(data=[go.Bar(x=['A', 'B', 'C'], y=[1, 3, 2])])
fig.update_layout(title='<b>Graphs -Bold Title</b>')
fig.show()

import plotly.graph_objects as go

fig = go.Figure(data=[go.Table(
	header=dict(values=['A', 'B']),
	cells=dict(values=[[10, 20, 30, 40],
					[40, 20, 10, 50]]))
])
fig.show()

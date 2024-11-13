import plotly.graph_objects as go

fig = go.Figure(data=go.Parcoords(
	line_color='green',
	dimensions=list([
		dict(range=[4, 9],
			label='A', values=[5, 8]),
		dict(range=[2, 7],
			label='B', values=[3, 6]),
	])
)
)

fig.show()

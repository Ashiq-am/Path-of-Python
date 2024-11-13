import plotly.graph_objects as go

fig = go.Figure(go.Carpet(
	a = [1, 2, 3, 1, 2, 3],
	b = [4, 5, 6, 4, 5, 6],
	y = [1, 2, 3, 4, 5, 6]
))

fig.show()

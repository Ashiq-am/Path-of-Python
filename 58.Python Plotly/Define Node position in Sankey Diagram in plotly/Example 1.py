import plotly.graph_objects as go


plot = go.Figure(go.Sankey(
	node = {
		"label": ["A", "B", "C"],
		"x": [0.5, 0.2, 0.1],
		"y": [0.4, 0.3, 0.7],
		'pad':5},
	link = {
		"source": [1, 0, 1],
		"target": [2, 3, 4],
		"value": [4, 2, 1]}))

plot.show()

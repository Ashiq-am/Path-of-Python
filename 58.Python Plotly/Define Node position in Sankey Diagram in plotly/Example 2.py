import plotly.graph_objects as go


plot = go.Figure(go.Sankey(
	node = {
		"label": ["Geeks", "For", "Geeks", "GFG"],
		"x": [0.5, 0.2, 0.1, 0.9],
		"y": [0.6, 0.8, 0.7],
		"color": "green",
		'pad':5},
	link = {
		"source": [3, 2, 1],
		"target": [5, 3, 7],
		"value": [6, 1, 2]}))

plot.show()

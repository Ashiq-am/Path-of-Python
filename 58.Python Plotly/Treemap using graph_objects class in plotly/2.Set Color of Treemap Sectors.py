import plotly.graph_objects as go

fig = go.Figure(go.Treemap(
	labels = ["A", "B", "C", "D", "E"],
	parents = ["", "A", "B", "C", "A"],
	marker_colors = ["blue", "pink", "red",
				"royalblue", "lightgray", ]
))

fig.show()

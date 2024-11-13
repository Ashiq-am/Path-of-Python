import plotly.graph_objects as go

fig = go.Figure(go.Treemap(
	labels = ["A", "B", "C", "D", "E"],
	parents = ["", "A", "B", "C", "A"],
marker_colors = ["blue", "pink"]
))

fig.update_layout(uniformtext = dict(minsize = 15,
								mode ='hide'))

fig.show()

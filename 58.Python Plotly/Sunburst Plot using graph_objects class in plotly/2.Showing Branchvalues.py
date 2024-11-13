import plotly.graph_objects as go

fig = go.Figure(go.Sunburst(
	labels =["A", "B", "C", "D", "E", "F", "G", "H", "I"],
	parents =["", "A", "A", "C", "C", "A", "A", "G", "A" ],
	values =[11, 24, 2, 6, 7, 1, 1, 5, 4],
	branchvalues ="remainder",
))

fig.update_layout(margin = dict(t = 0, l = 0, r = 0, b = 0))

fig.show()

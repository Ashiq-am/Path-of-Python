import plotly.figure_factory as ff


z = [[0.300000, 0.00000, 0.65, 0.300000],
	[1, 0.100005, 0.45, 0.4300],
	[0.300000, 0.00000, 0.65, 0.300000],
	[1, 0.100005, 0.45, 0.00000]]
fig = ff.create_annotated_heatmap(z)
fig.show()

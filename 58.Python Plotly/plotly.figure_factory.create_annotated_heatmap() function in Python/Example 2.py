import plotly.figure_factory as ff

z = [[.1, .3, .5, .7],
	[1, .8, .6, .4],
	[.6, .4, .2, .0],
	[.9, .7, .5, .3]]

fig = ff.create_annotated_heatmap(z, colorscale='Viridis')
fig.show()

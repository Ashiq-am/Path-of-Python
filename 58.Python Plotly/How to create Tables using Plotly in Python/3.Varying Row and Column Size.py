import plotly.graph_objects as go

color1 = 'lightgreen'
color2 = 'lightblue'

fig = go.Figure(data=[go.Table(
	# Ratio for column width
	columnwidth=[1, 5],
	header=dict(values=['A', 'B']),
	cells=dict(values=[[10, 20, 30, 40],
					[40, 20, 10, 50]],
			fill_color=[[color1, color2, color1,
							color2, color1]*2],))
])
fig.show()

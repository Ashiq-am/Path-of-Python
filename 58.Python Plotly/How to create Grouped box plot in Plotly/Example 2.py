import plotly.graph_objects as go


fig = go.Figure()

# Defining y axis
y = ['a', 'a', 'a', 'b', 'b', 'b']

fig.add_trace(go.Box(

	# defining x axis in corresponding
	# to y-axis
	y=y,
	x=[1, 2, 6, 4, 5, 6],
	name='A',
	marker_color='green'
))

fig.add_trace(go.Box(
	y=y,
	x=[2, 3, 4, 1, 2, 6],
	name='B',
	marker_color='yellow'
))

fig.add_trace(go.Box(
	y=y,
	x=[2, 5, 6, 7, 8, 1],
	name='C',
	marker_color='blue'
))

fig.update_layout(

	# group together boxes of the different
	# traces for each value of y
	boxmode='group'
)

# changing the orientation to horizontal
fig.update_traces(orientation='h')

fig.show()

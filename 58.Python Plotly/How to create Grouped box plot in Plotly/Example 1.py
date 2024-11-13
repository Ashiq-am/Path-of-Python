import plotly.graph_objects as go


fig = go.Figure()

# Defining x axis
x = ['a', 'a', 'a', 'b', 'b', 'b']

fig.add_trace(go.Box(

	# defining y axis in corresponding
	# to x-axis
	y=[1, 2, 6, 4, 5, 6],
	x=x,
	name='A',
	marker_color='green'
))

fig.add_trace(go.Box(
	y=[2, 3, 4, 1, 2, 6],
	x=x,
	name='B',
	marker_color='yellow'
))

fig.add_trace(go.Box(
	y=[2, 5, 6, 7, 8, 1],
	x=x,
	name='C',
	marker_color='blue'
))

fig.update_layout(

	# group together boxes of the different
	# traces for each value of x
	boxmode='group'
)
fig.show()

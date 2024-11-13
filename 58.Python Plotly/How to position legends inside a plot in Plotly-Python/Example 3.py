import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
	x=[1, 2, 3, 4, 5],
	y=[1, 2, 3, 4, 5],
	mode='markers',
	marker={'size': 10}
))

# plotting the scatter chart
fig.add_trace(go.Scatter(
	x=[1, 2, 3, 4, 5],
	y=[5, 4, 3, 2, 1],
	mode='markers',
	marker={'size': 100}
))

# position legends inside a plot
fig.update_layout(
	legend=dict(
		x=.9, # value must be between 0 to 1.
		y=1, # value must be between 0 to 1.
		traceorder="normal",
		font=dict(
			family="sans-serif",
			size=12,
			color="black"
		),
	)
)

fig.update_layout(legend={'itemsizing': 'constant'})

fig.show()

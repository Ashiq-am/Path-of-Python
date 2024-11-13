# importing packages
import plotly.graph_objects as go

# using medals_wide dataset
fig = go.Figure()

# plotting the scatter chart
fig.add_trace(go.Scatter(
	x=[1, 2, 3, 4, 5],
	y=[1, 2, 3, 4, 5],
))

# plotting the scatter chart
fig.add_trace(go.Scatter(
	x=[1, 2, 3, 4, 5],
	y=[5, 4, 3, 2, 1],
	visible='legendonly'
))

# position legends inside a plot
fig.update_layout(
	legend=dict(
		x=0.6, # value must be between 0 to 1.
		y=1, # value must be between 0 to 1.
		traceorder="normal",
		font=dict(
			family="sans-serif",
			size=12,
			color="black"
		),
	)
)

fig.show()

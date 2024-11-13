import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Bar(x=[1, 2, 3], y=[4, 5, 6],
					name="yaxis1 data", yaxis='y'))

fig.add_trace(go.Scatter(x=[2, 3, 5], y=[40, 50, 60],
						name="yaxis2 data", yaxis="y2"))

fig.add_trace(go.Bar(x=[4, 5, 6], y=[40000, 50000, 60000],
					name="yaxis3 data", yaxis="y3"))

# Create axis objects
fig.update_layout(xaxis=dict(domain=[0.3, 0.7]),

				# create 1st y axis
				yaxis=dict(
	title="yaxis title",
	titlefont=dict(color="#1f77b4"),
	tickfont=dict(color="#1f77b4")),

	# create 2nd y axis
	yaxis2=dict(title="yaxis2 title", overlaying="y",
				side="left", position=0.15),

	# create 3rd y axis
	yaxis3=dict(
		title="yaxis3 title",
		anchor="x", overlaying="y", side="right"))


# title
fig.update_layout(
	title_text="Geeksforgeeks - Three y-axes",
	width=800,
)

fig.show()

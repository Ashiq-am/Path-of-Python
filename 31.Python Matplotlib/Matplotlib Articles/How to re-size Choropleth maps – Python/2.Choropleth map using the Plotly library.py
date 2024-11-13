# import ploty libraray
import plotly.graph_objects as go

# create figure using fig method
fig = go.Figure(data=go.Choropleth(
	locations=['CA', 'TX', 'NY'],
	z=[1, 2, 3],
	locationmode='USA-states',
	colorscale='Viridis',
))

# Resize the code using
# update layout figure method
fig.update_layout(
	title_text='GeeksforGeeks',
	geo=dict(scope='usa', showlakes=True,
			lakecolor='rgb(85,173,240)'),
	width=500,
	height=500,
)

#show map
fig.show()

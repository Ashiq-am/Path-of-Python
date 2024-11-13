import plotly.graph_objects as go
import plotly.express as px

df = px.data.tips()

fig = go.Figure(data=go.Parcoords(
	dimensions=list([
		dict(range=[0, 8],
			constraintrange=[4, 8],
			label='Sepal Length', values=df['tip']),
		dict(range=[0, 8],
			label='Sepal Width', values=df['total_bill']),
	])
)
)


fig.show()

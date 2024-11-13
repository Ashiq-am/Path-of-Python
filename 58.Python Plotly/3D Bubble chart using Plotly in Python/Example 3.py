import plotly.express as px
import plotly.graph_objects as go


df = px.data.tips()

fig = go.Figure(go.Scatter3d(
	x = df['total_bill'],
	y = df['time'],
	z = df['day'],
	mode = 'markers',
	marker = dict(
		color = df['tip'],
		size = df['total_bill'],
		colorscale=[[0, 'rgb(15, 10, 172)'],
					[.3, 'rgb(150, 255, 255)'],
					[1, 'rgb(100, 10, 100)']]
		)
))

fig.show()

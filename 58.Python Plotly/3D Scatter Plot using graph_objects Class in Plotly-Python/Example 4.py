import plotly.express as px
import plotly.graph_objects as go

df = px.data.tips()

fig = go.Figure(data =[go.Scatter3d(x = df['total_bill'],
								y = df['time'],
								z = df['day'],
								mode ='markers',
								marker = dict(
									color = df['tip'],
									colorscale ='Viridis',
									opacity = 0.5
								)
)])
fig.show()

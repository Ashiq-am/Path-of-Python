import plotly.express as px
import plotly.graph_objects as go

df = px.data.tips()

fig = go.Figure(data =[go.Scatter3d(x = df['total_bill'],
								y = df['time'],
								z = df['tip'],
								mode ='markers')])
fig.show()

import plotly.express as px

df = px.data.tips()

fig = px.scatter_3d(df, x = 'total_bill',
					y = 'day',
					z = 'time',
					color = 'sex',
					size='tip',
					size_max = 20,
					opacity = 0.7)

fig.show()

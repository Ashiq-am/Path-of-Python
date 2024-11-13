import plotly.express as px

df = px.data.tips()

plot = px.line_3d(df, x = 'time',
				y = 'day',
				z = 'sex',
				color = 'time')
plot.show()

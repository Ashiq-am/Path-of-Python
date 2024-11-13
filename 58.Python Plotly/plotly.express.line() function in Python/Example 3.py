import plotly.express as px

df = px.data.tips()

plot = px.line(df, x = 'time',
			y = 'total_bill',
			color = 'sex',
			line_group = 'day')

plot.show()

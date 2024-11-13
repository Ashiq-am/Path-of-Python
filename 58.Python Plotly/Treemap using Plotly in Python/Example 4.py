import plotly.express as px

df = px.data.tips()

fig = px.treemap(df, path=['day', 'time', 'tip'],
				values='total_bill',
				color='sex')

fig.show()

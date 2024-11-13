import plotly.express as px

df = px.data.iris()

fig = px.sunburst(df, path=['sepal_length',
							'sepal_width',
							'petal_length'],
				values='petal_width')
fig.show()

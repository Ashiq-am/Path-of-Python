import plotly.express as px

df = px.data.iris()

plot = px.line_ternary(df, a = 'sepal_width',
						b = 'sepal_length',
						c = 'petal_width',
						color = 'species',
						line_group = 'species')
plot.show()

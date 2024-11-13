import plotly.express as px

df = px.data.iris()

plot = px.scatter_ternary(df, a = 'sepal_width',
						b = 'sepal_length',
						c = 'petal_width')
plot.show()

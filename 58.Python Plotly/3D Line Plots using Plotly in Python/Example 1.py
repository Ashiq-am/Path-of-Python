import plotly.express as px


df = px.data.iris()

fig = px.line_3d(df, x="sepal_width",
				y="petal_length",
				z="petal_width")
fig.show()

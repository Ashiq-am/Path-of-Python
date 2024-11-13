import plotly.express as px

df = px.data.iris().head(20)

fig = px.line(df, x = "sepal_width",
			y = "sepal_length" ,
			color = "sepal_length")
fig.show()

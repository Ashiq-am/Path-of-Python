import plotly.express as px

# Loading the iris dataset
df = px.data.iris()

fig = px.line(df, x = "sepal_width", y = "sepal_length",
			color = "species")
fig.show()

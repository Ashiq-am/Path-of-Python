import plotly.express as px

# Loading the iris dataset
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length",
				color="species", size='petal_length',
				hover_data=['petal_width'])
fig.show()

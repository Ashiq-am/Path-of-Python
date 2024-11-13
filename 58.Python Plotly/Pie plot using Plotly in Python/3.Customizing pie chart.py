import plotly.express as px

# Loading the iris dataset
df = px.data.iris()

fig = px.pie(df, values="sepal_width", names="species",
			title='Iris Dataset', hover_data=['sepal_length'])
fig.show()

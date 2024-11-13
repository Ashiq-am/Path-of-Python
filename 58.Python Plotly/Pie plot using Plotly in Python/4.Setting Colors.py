import plotly.express as px

# Loading the iris dataset
df = px.data.iris()

fig = px.pie(df, values="sepal_width",
			names="species",
			color_discrete_sequence=px.colors.sequential.RdBu)
fig.show()

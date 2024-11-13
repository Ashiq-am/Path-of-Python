import plotly.express as px

# Loading the iris dataset
df = px.data.iris()

fig = px.bar(df, x="sepal_width", y="sepal_length")
fig.show()

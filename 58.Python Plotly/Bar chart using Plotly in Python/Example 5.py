import plotly.express as px

df = px.data.iris()

fig = px.bar(df, x="sepal_width", y="sepal_length",
			color="species", barmode="group",
			facet_row="species", facet_col="species_id")

fig.show()

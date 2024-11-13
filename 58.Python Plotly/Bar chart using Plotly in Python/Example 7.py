import plotly.express as px

df = px.data.iris()

fig = px.bar(df, x="sepal_width", y="sepal_length",
			color="species", barmode = 'group')
fig.show()

import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")

fig = px.line(df, x="year", y="lifeExp", color="country")
fig.update_traces(mode="markers+lines")

fig.show()

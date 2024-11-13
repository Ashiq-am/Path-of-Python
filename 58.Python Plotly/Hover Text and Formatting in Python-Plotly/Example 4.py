import plotly.express as px

df_2007 = px.data.gapminder().query("year==2007")

fig = px.scatter(df_2007, x="gdpPercap", y="lifeExp",
				log_x=True, color='continent')

fig.update_traces(hovertemplate='GDP: %{x} <br>Life Expectancy: %{y}')

fig.show()

import plotly.express as px


df = px.data.gapminder().query("year == 2007")

plot = px.scatter_geo(df, locations="iso_alpha",
					size="gdpPercap",
					color = "country")
plot.show()

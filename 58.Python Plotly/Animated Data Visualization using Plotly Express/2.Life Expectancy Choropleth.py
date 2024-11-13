import plotly.express as px


gapminder = px.data.gapminder()
gapminder.head(15)

fig = px.choropleth(gapminder,
					locations ="iso_alpha",
					color ="lifeExp",
					hover_name ="country",
					color_continuous_scale = px.colors.sequential.Plasma,
					scope ="world",
					animation_frame ="year")
fig.show()

import plotly.express as px


gapminder = px.data.gapminder()
gapminder.head(15)

fig = px.scatter(
	gapminder,
	x ="gdpPercap",
	y ="lifeExp",
	animation_frame ="year",
	animation_group ="country",
	size ="pop",
	color ="continent",
	hover_name ="country",
	facet_col ="continent",
	size_max = 45,
	range_y =[25, 90]
)
fig.show()

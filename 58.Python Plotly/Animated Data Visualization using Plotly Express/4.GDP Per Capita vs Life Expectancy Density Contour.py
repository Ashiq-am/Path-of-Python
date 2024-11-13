import plotly.express as px


gapminder = px.data.gapminder()
gapminder.head(15)

fig = px.density_contour(gapminder,
						x ="gdpPercap",
						y ="lifeExp",
						color ="continent",
						marginal_y ="histogram",
						animation_frame ='year',
						animation_group ='country',
						range_y =[25, 100])
fig.show()

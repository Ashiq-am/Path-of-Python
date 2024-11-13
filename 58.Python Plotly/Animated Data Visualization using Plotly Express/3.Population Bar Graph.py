import plotly.express as px


gapminder = px.data.gapminder()
gapminder.head(15)

fig = px.bar(gapminder,
			x ="continent",
			y ="pop",
			color ='lifeExp',
			animation_frame ='year',
			hover_name ='country',
			range_y =[0, 4000000000])
fig.show()

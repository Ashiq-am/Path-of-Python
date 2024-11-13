# importing packages
import plotly.express as px

# using the gapminder dataset
data = px.data.gapminder()
data_canada = data[data.country == 'Canada']

# plotting the bar chart
fig = px.scatter(data_canada, x='year', y='pop',
			hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
			labels={'pop':'population of Canada'}, height=400, title="Geeksforgeeks")

# hiding color-bar
fig.update_coloraxes(showscale=False)

fig.show()

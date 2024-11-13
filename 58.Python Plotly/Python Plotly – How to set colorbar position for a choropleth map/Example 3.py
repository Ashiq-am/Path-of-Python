# importing packages
import plotly.express as px

# using the gapminder dataset
data = px.data.gapminder()
data_canada = data[data.country == 'Canada']

# plotting the bar chart
fig = px.scatter(data_canada, x='year', y='pop',
				hover_data=['lifeExp', 'gdpPercap'],
				color='lifeExp',
				labels={'pop': 'population of Canada'},
				height=400, title="Geeksforgeeks")

# set colorbar position for X-axis
fig.update_layout(coloraxis_colorbar_x=0.9)

# set colorbar position for Y-axis
fig.update_layout(coloraxis_colorbar_y=0.1)

fig.show()

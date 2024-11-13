px.scatter(dataset1.head(10), x='Country/Region', y= 'TotalDeaths',
		hover_data=['Country/Region', 'Continent'],
		color='Country/Region', size= 'TotalDeaths', size_max=80)

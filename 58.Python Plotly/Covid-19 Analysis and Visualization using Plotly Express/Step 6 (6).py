px.scatter(dataset1.head(30), x='TotalCases', y= 'TotalDeaths',
		hover_data=['Country/Region', 'Continent'],
		color='TotalDeaths', size= 'TotalDeaths', size_max=80,
		log_x=True, log_y=True)

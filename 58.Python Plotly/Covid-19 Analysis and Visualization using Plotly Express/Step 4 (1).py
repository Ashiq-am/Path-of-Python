px.bar(dataset1.head(15), x = 'Country/Region', y = 'TotalCases',
	color = 'TotalDeaths', height = 500,
	hover_data = ['Country/Region', 'Continent'])

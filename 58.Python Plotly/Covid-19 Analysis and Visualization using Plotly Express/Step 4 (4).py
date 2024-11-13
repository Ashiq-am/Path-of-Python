px.bar(dataset1.head(15), x = 'TotalTests', y = 'Country/Region',
	color = 'TotalTests',orientation ='h', height = 500,
	hover_data = ['Country/Region', 'Continent'])

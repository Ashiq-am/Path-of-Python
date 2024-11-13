px.bar(dataset1.head(15), x = 'TotalTests', y = 'Continent',
	color = 'TotalTests',orientation ='h', height = 500,
	hover_data = ['Country/Region', 'Continent'])

px.scatter(dataset1.head(30), x='TotalTests', y= 'TotalCases',
		hover_data=['Country/Region', 'Continent'],
		color='TotalTests', size= 'TotalTests', size_max=80,
		log_x=True, log_y=True)

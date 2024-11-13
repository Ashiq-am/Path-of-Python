px.scatter(dataset1.head(50), x='Continent',y='TotalTests',
		hover_data=['Country/Region', 'Continent'],
		color='TotalTests', size='TotalTests', size_max=80, log_y=True)

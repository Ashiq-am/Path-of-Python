px.scatter(dataset1.head(57), x='Continent',y='TotalCases',
		hover_data=['Country/Region', 'Continent'],
		color='TotalCases', size='TotalCases', size_max=80, log_y=True)

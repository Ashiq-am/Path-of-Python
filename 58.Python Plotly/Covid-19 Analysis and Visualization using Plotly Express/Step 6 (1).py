px.scatter(dataset1.head(30), x='Country/Region', y='TotalCases',
		hover_data=['Country/Region', 'Continent'],
		color='Country/Region', size='TotalCases', size_max=80, log_y=True)

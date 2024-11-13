px.scatter(dataset1.head(100), x='Country/Region', y='TotalCases',
		hover_data=['Country/Region', 'Continent'],
		color='TotalCases', size='TotalCases', size_max=80)

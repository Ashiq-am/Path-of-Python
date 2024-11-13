px.scatter(dataset1.head(30), x='Country/Region', y= 'Tests/1M pop',
		hover_data=['Country/Region', 'Continent'],
		color='Country/Region', size= 'Tests/1M pop', size_max=80)

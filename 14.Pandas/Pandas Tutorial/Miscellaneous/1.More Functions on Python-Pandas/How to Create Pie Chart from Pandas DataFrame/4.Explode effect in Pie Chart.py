import pandas as pd

# DataFrame of each student and the votes they get
dataframe = pd.DataFrame({'Name': ['Aparna', 'Aparna', 'Aparna',
								'Aparna', 'Aparna', 'Juhi',
								'Juhi', 'Juhi', 'Juhi', 'Juhi',
								'Suprabhat', 'Suprabhat',
								'Suprabhat', 'Suprabhat',
								'Suprabhat'],
						'votes_of_each_class': [12, 9, 17, 19,
												20, 11, 15, 12,
												9, 4, 22, 19, 17,
												19, 18]})

# Defining colors for the pie chart
colors = ['pink', 'silver', 'steelblue']

# Define the ratio of gap of each fragment in a tuple
explode = (0.05, 0.05, 0.05)

# Plotting the pie chart for above dataframe
dataframe.groupby(['Name']).sum().plot(
	kind='pie', y='votes_of_each_class', autopct='%1.0f%%',
colors=colors, explode=explode)

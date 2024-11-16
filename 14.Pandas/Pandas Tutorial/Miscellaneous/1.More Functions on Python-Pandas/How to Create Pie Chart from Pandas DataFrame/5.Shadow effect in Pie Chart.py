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


# Plotting the pie chart for above dataframe
# and implementing shadow effect
dataframe.groupby(['Name']).sum().plot(
	kind='pie', y='votes_of_each_class', autopct='%1.0f%%', shadow=True)

# import necessary packages
import pandas as pd

# create a dataframe
data = pd.DataFrame({'Name': ['Akhil', 'Nikhil', 'Satyam', 'Sravan', 'Pavan'],
					'Marks': [77, 95, 89, 78, 64],
					'Credits': [8, 10, 9, 8, 7]})

# box plot for marks column
data.boxplot(column='Marks')

# import necessary packages
import pandas as pd
import matplotlib.pyplot as plt

# create a dataframe
data = pd.DataFrame({'Name': ['Akhil', 'Nikhil', 'Satyam', 'Sravan', 'Pavan'],
					'Marks': [77, 95, 89, 78, 10],
					'Credits': [8, 10, 9, 8, 0]})

# outlier box plot
data['Marks'].plot(kind='box', title='Marks of students')
plt.show()

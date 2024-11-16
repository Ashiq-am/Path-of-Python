# import necessary packages
import pandas as pd
import matplotlib.pyplot as plt

# create a dataframe
data = pd.DataFrame({'Name': ['Akhil', 'Nikhil', 'Satyam', 'Sravan', 'Pavan'],
					'Marks': [77, 95, 89, 78, 64],
					'Credits': [8, 10, 9, 8, 7]})

# box plot
data['Marks'].plot(kind='box', title='Marks of students')
plt.show()

# importing the module
import pandas as pd

# creating the DataFrame
df = pd.DataFrame({'Name' : ['Mukul', 'Rohan', 'Mayank',
							'Sundar', 'Aakash'],
				'Course' : ['BCA', 'BBA', 'BCA', 'MBA', 'BBA'],
				'Location' : ['Saharanpur', 'Meerut', 'Agra',
								'Saharanpur', 'Meerut']})

# counting the duplicates
dups = df.pivot_table(index = ['Course', 'Location'], aggfunc ='size')

# displaying the duplicate Series
print(dups)

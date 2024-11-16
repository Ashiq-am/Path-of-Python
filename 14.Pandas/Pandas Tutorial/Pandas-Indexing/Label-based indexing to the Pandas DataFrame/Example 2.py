# importing pandas library
import pandas as pd

# Creating a Data frame
df = pd.DataFrame([['1993', 'Avi', 5, 41, 70, 'Bob'],
				['1994', 'Cathy', 10, 1, 22, 'Cathy'],
				['1995', 'Cathy', 24, 11, 44, 'Bob'],
				['1996', 'Bob', 2, 11, 10, 'Avi'],
				['1998', 'Avi', 20, 10, 40, 'Avi'],
				['1999', 'Avi', 50, 8, 11, 'Cathy']],
				columns=('Patients', 'Name', 'Avi', 'Bob', 'Cathy', 'Aname'))

# Display Data frame
df

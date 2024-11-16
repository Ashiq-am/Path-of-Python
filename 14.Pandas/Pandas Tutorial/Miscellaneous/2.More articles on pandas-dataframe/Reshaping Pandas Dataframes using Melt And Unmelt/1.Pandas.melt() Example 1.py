# importing pandas library
import pandas as pd

# creating and initializing a list
values = [['Monday', 65000, 50000],
		['Tuesday', 68000, 45000],
		['Wednesday', 70000, 55000],
		['Thursday', 60000, 47000],
		['Friday', 49000, 25000],
		['Saturday', 54000, 35000],
		['Sunday', 100000, 70000]]

# creating a pandas dataframe
df = pd.DataFrame(values, columns=['DAYS', 'PATIENTS', 'RECOVERY'])

# displaying the data frame
df

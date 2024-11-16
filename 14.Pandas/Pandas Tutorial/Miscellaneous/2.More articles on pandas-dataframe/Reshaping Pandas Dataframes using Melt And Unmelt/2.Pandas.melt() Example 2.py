# importing pandas library
import pandas as pd

# creating and initializing a dataframe
values = [['Monday', 65000, 50000, 1500],
		['Tuesday', 68000, 45000, 7250],
		['Wednesday', 70000, 55000, 1400],
		['Thursday', 60000, 47000, 4200],
		['Friday', 49000, 25000, 3000],
		['Saturday', 54000, 35000, 2000],
		['Sunday', 100000, 70000, 4550]]

# creating a pandas dataframe
df = pd.DataFrame(values,
				columns=['DAYS', 'PATIENTS', 'RECOVERY', 'DEATHS'])

# displaying the data frame
df

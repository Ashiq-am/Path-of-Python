# Importing pandas libraray
import pandas as pd

# Loading dataframes
dataframe1 = pd.DataFrame({'empname': ['rohan', 'hina', 'alisa', ],
						'department': ['IT', 'admin', 'finance', ],
						'designation': ['Sr.developer', 'administrator', 'executive', ]})

dataframe2 = pd.DataFrame({'empname': ['rishi', 'huma', 'alisa', ],
						'department': ['cyber security', 'HR', 'finance', ],
						'designation': ['penetration tester', 'HR executive', 'executive', ]})

# Concatenating two dataframes wtithout duplicates
new_dataframe = pd.concat([dataframe1, dataframe2]).drop_duplicates()

# Resetting index
new_dataframe = new_dataframe.reset_index(drop=True)

# Display dataframe generated
new_dataframe

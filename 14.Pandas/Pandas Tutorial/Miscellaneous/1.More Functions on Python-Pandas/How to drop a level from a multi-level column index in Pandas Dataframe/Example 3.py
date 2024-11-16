# importing all important libraries
import pandas as pd

# Creating a pandas dataframe
df = pd.DataFrame([["Coding", "System Design"],
				["DBMS", "Aptitude"],
				["Logical Reasoning", "Development"]])

# Creating multilevel index from tuples
df.columns = pd.MultiIndex.from_tuples([('Group 1', 'Group 2', 'Group 3', 'Group 4'),
										('Group 3', 'Group 4', 'Group 5', 'Group 6')],
									names=['level 1', 'level 2', 'level 3', 'level 4'])
# Showing the dataframe
print(df)

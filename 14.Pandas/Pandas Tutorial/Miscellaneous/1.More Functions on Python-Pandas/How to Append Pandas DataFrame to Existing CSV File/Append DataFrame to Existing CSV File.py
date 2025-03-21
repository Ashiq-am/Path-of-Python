# Append Pandas DataFrame to Existing CSV File
# importing pandas module
import pandas as pd

# data of Player and their performance
data = {
	'Name': ['Hardik', 'Pollard', 'Bravo'],
	'Run': [50, 63, 15],
	'Wicket': [0, 2, 3],
	'Catch': [4, 2, 1]
}

# Make data frame of above data
df = pd.DataFrame(data)

# append data frame to CSV file
df.to_csv('GFG.csv', mode='a', index=False, header=False)

# print mesaage
print("Data appended successfully.")

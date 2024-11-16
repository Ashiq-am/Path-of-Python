# importing pandas as pd
import pandas as pd

# reading csv file
df = pd.read_csv("Assignment.csv")

# filtering the rows where job is Govt
for index, row in df.iterrows():
	if 'Govt' in row['job']:
		print(index, row['job'], row['Age_Range'],
			row['Salary'], row['Savings'], row['Credit-Rating'])

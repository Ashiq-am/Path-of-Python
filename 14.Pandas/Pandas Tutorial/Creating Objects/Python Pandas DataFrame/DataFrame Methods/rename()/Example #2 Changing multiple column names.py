# importing pandas module
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name" )


# changing cols with rename()
new_data = data.rename(columns = {"Team": "Team Name",
								"College":"Education",
								"Salary": "Income"})

# changing columns using .columns()
data.columns = ['Team Name', 'Number', 'Position', 'Age',
				'Height', 'Weight', 'Education', 'Income']

# dropna used to ignore na values
print(new_data.dropna()== data.dropna())

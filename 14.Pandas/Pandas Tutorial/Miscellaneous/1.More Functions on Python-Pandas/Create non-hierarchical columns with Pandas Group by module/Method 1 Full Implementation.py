"""
Program: For each "Sector" and "Industry" Find the total, average employees, and the minimum, maximum revenue change.
"""

import pandas as pd

""" 
Function: Convert hierarchial columns to non-hierarchial columns 
params: dataframe with hierarchial columns 
return : dataframe with non-hierarchial columns 
"""


def return_non_hierarchial(df):
	df.columns = ['_'.join(x) for x in df.columns.to_flat_index()]
	return df


# load the dataset with rank as index
df = pd.read_csv("https://raw.githubusercontent.com/sasankac/TestDataSet/master/Fortune500.csv", index_col="Rank")

# remove unwanted columns
remove_columns = ['Website', 'Hqaddr', 'Hqzip', 'Hqtel', 'Ceo',
				'Ceo-title', 'Address', 'Ticker', 'Prftchange',
				'Assets', 'Totshequity']

df = df.drop(columns=remove_columns, axis=1)

# Identify the data as per the requirement
df_result = (df
			.groupby(['Sector', 'Industry'])
			.agg({'Employees': ['sum', 'mean'],
				'Revchange': ['min', 'max']})
			.astype(int)
			.pipe(return_non_hierarchial))

# print the data
df_result.head(15)

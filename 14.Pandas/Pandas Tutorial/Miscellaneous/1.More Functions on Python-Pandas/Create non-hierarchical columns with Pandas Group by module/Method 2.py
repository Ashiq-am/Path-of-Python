"""
Program: For each "Sector" and "Industry" Find the total, average employees, and the minimum, maximum revenue change.
"""

import pandas as pd

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
			.agg(Employees_sum=pd.NamedAgg(column='Employees', aggfunc='sum'),
				Employees_average=pd.NamedAgg(
					column='Employees', aggfunc='mean'),
				Revchange_minimum=pd.NamedAgg(
					column='Revchange', aggfunc='min'),
				Revchange_maximum=pd.NamedAgg(column='Revchange', aggfunc='max'))
			.astype(int))

# print the data
df_result.head(15)

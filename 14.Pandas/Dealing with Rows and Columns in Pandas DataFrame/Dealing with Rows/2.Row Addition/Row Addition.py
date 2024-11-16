''''''
'''In Order to add a Row in Pandas DataFrame, we can concat the old dataframe with new one.'''

# importing pandas module
import pandas as pd

# making data frame
df = pd.read_csv("nba.csv", index_col="Name")

df.head(10)

new_row = pd.DataFrame({'Name': 'Geeks', 'Team': 'Boston', 'Number': 3,
                        'Position': 'PG', 'Age': 33, 'Height': '6-2',
                        'Weight': 189, 'College': 'MIT', 'Salary': 99999},
                       index=[0])
# simply concatenate both dataframes
df = pd.concat([new_row, df]).reset_index(drop=True)
df.head(5)

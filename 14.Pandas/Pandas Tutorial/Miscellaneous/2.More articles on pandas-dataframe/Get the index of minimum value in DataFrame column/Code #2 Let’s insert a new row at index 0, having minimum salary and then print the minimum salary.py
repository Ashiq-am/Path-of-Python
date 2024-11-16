# importing pandas module
import pandas as pd

# making data frame
df = pd.read_csv("nba.csv")

new_row = pd.DataFrame({'Name': 'Geeks', 'Team': 'Boston', 'Number': 3,
                        'Position': 'PG', 'Age': 33, 'Height': '6-2',
                        'Weight': 189, 'College': 'MIT', 'Salary': 99}
                       , index=[0])

df = pd.concat([new_row, df]).reset_index(drop=True)
df.head(5)

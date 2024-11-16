# importing pandas as pd
import pandas as pd

# Making data frame from the csv file
df = pd.read_csv("nba.csv")

# First column ='New_Team', this column
# will append '_GO' at the end of each team name.
# Second column ='Revised_Salary' will increase
# the salary of all employees by 10 %
df.assign(New_team = lambda x: df['Team']+'_GO',
		Revised_Salary = lambda x: df['Salary']
							+ df['Salary'] / 10)

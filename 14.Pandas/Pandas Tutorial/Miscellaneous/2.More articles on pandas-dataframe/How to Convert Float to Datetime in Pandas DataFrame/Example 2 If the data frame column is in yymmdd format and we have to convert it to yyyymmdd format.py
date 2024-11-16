# importing pandas library
import pandas as pd

# Initializing the nested list with
# Data set
player_list = [[180112.0,'Mathematics'],
			[180114.0,'English'],
			[180116.0,'Physics'],
			[180119.0,'Chemistry'],
			[180121.0,'French'],
			[180124.0,'Biology'],
			[180129.0,'Sanskrit']]

# creating a pandas dataframe
df = pd.DataFrame(player_list,columns=['Dates','Test'])

# printing dataframe
print(df)
print()

# checking the type
print(df.dtypes)

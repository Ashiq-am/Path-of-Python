# importing pandas library
import pandas as pd

# Initializing the nested list
# with Data set
player_list = [[20200112.0,'Mathematics'],
			[20200114.0,'English'],
			[20200116.0,'Physics'],
			[20200119.0,'Chemistry'],
			[20200121.0,'French'],
			[20200124.0,'Biology'],
			[20200129.0,'Sanskrit']]

# creating a pandas dataframe
df = pd.DataFrame(player_list,columns=['Dates','Test'])

# printing dataframe
print(df)
print()

# checking the type
print(df.dtypes)

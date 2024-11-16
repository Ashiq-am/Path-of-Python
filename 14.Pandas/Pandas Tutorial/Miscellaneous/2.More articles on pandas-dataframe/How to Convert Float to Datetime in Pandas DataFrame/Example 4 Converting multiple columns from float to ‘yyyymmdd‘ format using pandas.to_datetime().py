# importing pandas library
import pandas as pd

# Initializing the nested list with Data set
player_list = [[20200112.0,'Mathematics',20200113.0],
			[20200114.0,'English',20200115.0],
			[20200116.0,'Physics',20200117.0],
			[20200119.0,'Chemistry',20200120.0],
			[20200121.0,'French',20200122.0],
			[20200124.0,'Biology',20200125.0],
			[20200129.0,'Sanskrit',20200130.0]]

# creating a pandas dataframe
df = pd.DataFrame(player_list,columns=['Starting_Date','Test','Ending_Date'])

# printing dataframe
print(df)
print()

# checking the type
print(df.dtypes)

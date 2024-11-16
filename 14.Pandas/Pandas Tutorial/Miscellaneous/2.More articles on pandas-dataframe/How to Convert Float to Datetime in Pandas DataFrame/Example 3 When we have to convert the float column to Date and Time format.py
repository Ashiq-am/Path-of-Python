# importing pandas library
import pandas as pd

# Initializing the nested list with Data set
player_list = [[20200112082520.0,'Mathematics'],
			[20200114085020.0,'English'],
			[20200116093529.0,'Physics'],
			[20200119101530.0,'Chemistry'],
			[20200121104060.0,'French'],
			[20200124113541.0,'Biology'],
			[20200129125023.0,'Sanskrit']]

# creating a pandas dataframe
df = pd.DataFrame(player_list,columns=['Dates','Test'])

# printing dataframe
print(df)
print()

# checking the type
print(df.dtypes)

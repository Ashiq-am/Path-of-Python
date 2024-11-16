# importing pandas as pd
import pandas as pd

# creating the dataframe using pandas DataFrame
df = pd.DataFrame({'X':[1, 2, 3, 4, 5],
				'Y':[54, 12, 57, 48, 96],
				'Z':['a', 'b', 'c', 'd', 'e']})

# df['column_name'] = df.loc[start_row_index:end_row_index,
# ['column1','column2']].sum(axis = 1)
# summing columns X and Y for row from 1 - 3
df['Sum_of_row'] = df.loc[1 : 3,['X' , 'Y']].sum(axis = 1)
print(df)

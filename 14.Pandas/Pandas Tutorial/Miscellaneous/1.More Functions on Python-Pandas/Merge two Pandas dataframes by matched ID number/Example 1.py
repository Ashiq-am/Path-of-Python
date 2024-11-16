# import pandas as pd
import pandas as pd

# creating dataframes as df1 and df2
df1 = pd.DataFrame({'ID': [1, 2, 3, 5, 7, 8],
					'Name': ['Sam', 'John', 'Bridge',
							'Edge', 'Joe', 'Hope']})

df2 = pd.DataFrame({'ID': [1, 2, 4, 5, 6, 8, 9],
					'Marks': [67, 92, 75, 83, 69, 56, 81]})

# merging df1 and df2 by ID
# i.e. the rows with common ID's get
# merged i.e. {1,2,5,8}
df = pd.merge(df1, df2, on="ID")
print(df)

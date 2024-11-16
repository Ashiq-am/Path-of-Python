# importing pandas as pd
import pandas as pd

# creating dataframes
df1 = pd.DataFrame({'ID': [1, 2, 3, 4],
					'Name': ['John', 'Tom', 'Simon', 'Jose']})

df2 = pd.DataFrame({'ID': [1, 2, 3, 5],
					'Class': ['Second', 'Third', 'Fifth', 'Fourth']})

# merging df1 and df2 with merge function
df = pd.merge(df1, df2)
print(df)

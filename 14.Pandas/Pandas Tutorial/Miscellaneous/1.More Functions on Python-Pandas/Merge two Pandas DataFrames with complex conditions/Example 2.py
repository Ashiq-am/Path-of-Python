# importing pandas as pd
import pandas as pd

# creating dataframes
df1 = pd.DataFrame({'Name': ['John', 'Tom', 'Simon', 'Jose'],
					'Age': [5, 6, 4, 5]})

df2 = pd.DataFrame({'Name': ['John', 'Tom', 'Jose'],
					'Class': ['Second', 'Third', 'Fifth']})

# merging df1 and df2 with merge function
# with the common column as Name
df = pd.merge(df1, df2, on='Name')
print(df)

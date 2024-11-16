import pandas as pd
data = {'A': [1.0, 2.4, 3.0],
		'B': [4.0, 5.0, 6.5]}

print("Before converting")
print(df.dtypes)
# Use apply method to convert Pandas columns to int
df_int = df.apply(lambda column: column.astype(int))

# Check the data types of columns
print("\nAfter converting")
print(df_int.dtypes)

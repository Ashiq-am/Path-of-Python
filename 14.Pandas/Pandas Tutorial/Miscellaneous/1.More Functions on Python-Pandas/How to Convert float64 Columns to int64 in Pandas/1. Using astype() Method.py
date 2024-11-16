import pandas as pd

# Create a sample DataFrame
data = {'A': [1.0, 2.0, 3.0],
		'B': [4.0, 5.0, 6.0]}
df = pd.DataFrame(data)

print("Before converting")
print(df.dtypes)

# Convert float64 columns to int64 using astype()
df['A'] = df['A'].astype('int64')
df['B'] = df['B'].astype('int64')

print("\nAfter converting")
# Check the data types of columns
print(df.dtypes)

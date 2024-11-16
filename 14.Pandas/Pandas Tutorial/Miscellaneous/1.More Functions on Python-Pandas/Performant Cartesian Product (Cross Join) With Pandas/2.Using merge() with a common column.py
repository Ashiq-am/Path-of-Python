import pandas as pd
# Create two DataFrames
df1 = pd.DataFrame(
	{'City': ['New York', 'Los Angeles'], 'Population': [8_398_748, 3_990_456]})
df2 = pd.DataFrame(
	{'State': ['New York', 'California'], 'Area (sq. mi)': [54_555, 163_696]})

# Adding a constant column to both DataFrames for cross join
df1['key'] = 1
df2['key'] = 1

# Performing the cross join
cartesian_product = pd.merge(df1, df2, on='key').drop('key', axis=1)

print(df1)
print(df2)
print("\nCross join:\n", cartesian_product)

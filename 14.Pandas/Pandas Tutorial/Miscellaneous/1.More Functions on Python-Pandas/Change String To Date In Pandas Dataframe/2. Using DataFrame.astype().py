import pandas as pd

# Example Data
data = {
	'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
	'Values': [100, 200, 300]
}

# Creating DataFrame
df = pd.DataFrame(data)

print("Before converting")
print(df.dtypes)

# Using DataFrame.astype()
df['Date'] = df['Date'].astype('datetime64[ns]')

print("\nAfter converting")
print(df.dtypes)

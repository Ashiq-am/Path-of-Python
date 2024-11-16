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

# Using pandas.to_datetime()
df['Date'] = pd.to_datetime(df['Date'])

print("\nAfter converting")
print(df.dtypes)


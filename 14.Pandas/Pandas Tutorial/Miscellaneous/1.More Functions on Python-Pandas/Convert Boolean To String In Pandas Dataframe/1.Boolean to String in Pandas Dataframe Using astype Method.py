import pandas as pd

# Sample DataFrame
data = {'column_name': [True, False, True, False]}
df = pd.DataFrame(data)

print('Before :', df.dtypes)

# Convert boolean to string using astype
df['column_name'] = df['column_name'].astype(str)

print(df)

print('After :', df.dtypes)

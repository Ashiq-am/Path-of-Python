import pandas as pd

# Sample DataFrame
data = {'column_name': [True, False, True, False]}
df = pd.DataFrame(data)

print('Before :', df.dtypes)

# Replace boolean values with strings using the replace method
df['column_name'] = df['column_name'].replace({True: 'True', False: 'False'})

# Display the DataFrame
print(df)

print('After :', df.dtypes)

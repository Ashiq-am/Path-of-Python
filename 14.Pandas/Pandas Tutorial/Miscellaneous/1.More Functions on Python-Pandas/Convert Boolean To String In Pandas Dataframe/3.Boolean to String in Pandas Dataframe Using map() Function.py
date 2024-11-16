import pandas as pd

# Sample DataFrame
data = {'column_name': [True, False, True, False]}
df = pd.DataFrame(data)

print('Before :',df.dtypes)
# Create a mapping dictionary for boolean to string
bool_to_str_mapping = {True: 'True', False: 'False'}

# Map boolean to string using map function
df['column_name'] = df['column_name'].map(bool_to_str_mapping)

# Display the DataFrame
print(df)

print('After :',df.dtypes)

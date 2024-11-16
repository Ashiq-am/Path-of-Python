import pandas as pd

# Sample DataFrame
data = {'column_name': [True, False, True, False]}
df = pd.DataFrame(data)

print('Before :',df.dtypes)

# Convert boolean to string using apply and lambda
df['column_name'] = df['column_name'].apply(lambda x: str(x))

# Display the DataFrame
print(df)

print('After :',df.dtypes)

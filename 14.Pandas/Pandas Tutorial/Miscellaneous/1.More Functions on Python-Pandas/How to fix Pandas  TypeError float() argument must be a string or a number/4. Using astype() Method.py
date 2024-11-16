import pandas as pd
data = {'values': ['10', '20', '30', '', '40']}
df = pd.DataFrame(data)

# Convert 'values' column to numeric type, coercing errors to NaN
df['values'] = pd.to_numeric(df['values'], errors='coerce')

# Fill NaN values with 0 (or another appropriate value)
df['values'].fillna(0, inplace=True)

# Convert 'values' column to integer type using astype()
df['values'] = df['values'].astype(int)
print(df)

import pandas as pd

# Create a DataFrame with NoneType values
data = {'values': ['10', '20', '30', None, '40']}
df = pd.DataFrame(data)

# Convert to numeric, setting errors='coerce' to handle NoneType values
df['values'] = pd.to_numeric(df['values'], errors='coerce')

# Fill NaN values with 0 (or another appropriate value)
df['values'].fillna(0, inplace=True)
print(df)

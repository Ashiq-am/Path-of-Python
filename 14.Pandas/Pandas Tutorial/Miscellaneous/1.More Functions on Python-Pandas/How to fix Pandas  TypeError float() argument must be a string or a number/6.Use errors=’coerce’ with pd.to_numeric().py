import pandas as pd

# Create a DataFrame with mixed data types
data = {'values': ['10', '20', '30', 'abc', None, '']}
df = pd.DataFrame(data)

# Convert to numeric, setting errors='coerce' to handle non-numeric values
df['values'] = pd.to_numeric(df['values'], errors='coerce')
print(df)

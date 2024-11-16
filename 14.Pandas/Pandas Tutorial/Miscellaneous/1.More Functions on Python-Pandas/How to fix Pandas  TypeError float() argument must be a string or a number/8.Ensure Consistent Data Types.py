import pandas as pd

# Create a DataFrame
data = {'values': ['10', '20', '30', '40']}
df = pd.DataFrame(data)

# Convert to float
df['values'] = df['values'].astype(float)
print(df.dtypes)

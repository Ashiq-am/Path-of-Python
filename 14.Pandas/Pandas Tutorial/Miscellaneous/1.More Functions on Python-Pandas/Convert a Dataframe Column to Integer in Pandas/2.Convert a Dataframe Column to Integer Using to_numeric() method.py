import pandas as pd

# Creating a sample DataFrame
data = {'Column1': ['1', '2', '3', '4']}
df = pd.DataFrame(data)

# Using to_numeric() method
df = pd.DataFrame(data)
df['Column1'] = pd.to_numeric(df['Column1'], downcast='integer', errors='coerce')
print(df)
df['Column1'].dtype

import pandas as pd

# Creating the DataFrames
df1 = pd.DataFrame({
    'Region': ['North', 'North'],
    'Product': ['Apples', 'Bananas'],
    'Sales': [120, 80]
})

df2 = pd.DataFrame({
    'Region': ['South', 'South'],
    'Product': ['Apples', 'Oranges'],
    'Sales': [100, 150]
})

# Concatenating rows
result = pd.concat([df1, df2], ignore_index=True)
print(result)
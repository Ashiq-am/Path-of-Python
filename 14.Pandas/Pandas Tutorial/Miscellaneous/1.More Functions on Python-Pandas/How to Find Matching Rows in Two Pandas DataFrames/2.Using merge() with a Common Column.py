import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['John', 'Alice', 'Bob', 'Eve']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4, 5],
    'Age': [25, 30, 22, 29]
})

# Perform inner join on the 'ID' column
result = pd.merge(df1, df2, on='ID', how='inner')
print(result)
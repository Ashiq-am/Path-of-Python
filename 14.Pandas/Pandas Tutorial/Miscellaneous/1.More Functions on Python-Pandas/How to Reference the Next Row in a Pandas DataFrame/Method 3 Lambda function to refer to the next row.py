import pandas as pd

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'],'Score': [85, 90, 88, 92]})

# Create a new column by referencing the next row using apply with lambda
df['Next_Score'] = df.apply(lambda row: df['Score'].iloc[row.name + 1] if row.name + 1 < len(df) else None,axis=1)
print(df)
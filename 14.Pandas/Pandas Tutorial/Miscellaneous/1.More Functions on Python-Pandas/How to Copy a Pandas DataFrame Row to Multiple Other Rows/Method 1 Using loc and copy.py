import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3],'B': [4, 5, 6]})

# Copy the second row (index 1) to multiple other rows
df.loc[3] = df.loc[1].copy()
df.loc[4] = df.loc[1].copy()

print(df)
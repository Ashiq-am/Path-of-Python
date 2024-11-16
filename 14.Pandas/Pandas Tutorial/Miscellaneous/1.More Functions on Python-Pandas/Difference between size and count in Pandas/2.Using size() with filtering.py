import pandas as pd

data = {'A': [1, 2, 3, None, 5]}
df = pd.DataFrame(data)

# Filtering rows where column 'A' is not null
filtered_df = df[df['A'].notnull()]
filtered_size = filtered_df.size

print(filtered_df)

print(filtered_size)

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3],'B': [4, 5, 6]})
new_rows = pd.DataFrame({'A': [9,10], 'B': [11,12]})

# Concatenate the new rows with the existing DataFrame
df = pd.concat([df, new_rows], ignore_index=True)
print(df)
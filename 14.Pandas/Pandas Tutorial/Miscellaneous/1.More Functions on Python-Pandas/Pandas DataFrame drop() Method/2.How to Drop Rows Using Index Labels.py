import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
df_dropped = df.drop(0, axis=0)
print(df_dropped)
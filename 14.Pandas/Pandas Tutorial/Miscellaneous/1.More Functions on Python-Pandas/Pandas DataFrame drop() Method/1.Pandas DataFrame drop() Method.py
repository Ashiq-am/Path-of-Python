import pandas as pd

df = pd.DataFrame({'A': [1, 2],'B': [4, 5],'C': [7, 8]})
print("Original DataFrame:\n", df)

df_dropped_col = df.drop(columns=['B']) # Dropping a column
print("\nDataFrame after dropping column 'B': \n", df_dropped_col)

df_dropped_row = df.drop(index=1) # Dropping a row
print("\nDataFrame after dropping row with index 1:\n", df_dropped_row)
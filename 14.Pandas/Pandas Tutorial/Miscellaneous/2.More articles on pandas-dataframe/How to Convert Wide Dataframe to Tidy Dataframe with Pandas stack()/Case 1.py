import pandas as pd

# Single level columns
df_single_level_cols = pd.DataFrame([[74, 80], [72, 85]],
									index=['Deepa', 'Balram'],
									columns=['Maths', 'Computer'])
print(df_single_level_cols)

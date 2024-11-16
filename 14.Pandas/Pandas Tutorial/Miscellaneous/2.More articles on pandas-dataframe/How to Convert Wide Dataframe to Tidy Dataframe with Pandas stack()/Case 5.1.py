# Drops the row with completely NaN values
df_multi_level_cols3.stack(dropna=True)
print(df_multi_level_cols3)

# Dropping missing values
df_multi_level_cols3 = pd.DataFrame([[None, 80], [77, 82]],
									index=['Deepa', 'Balram'],
									columns=multicol2)
print(df_multi_level_cols3)

# contains the row with all NaN values since,
# dropna=False
df_multi_level_cols3.stack(dropna=False)
print(df_multi_level_cols3)

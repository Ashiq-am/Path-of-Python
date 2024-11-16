# Simple Multi-level columns
multicol1 = pd.MultiIndex.from_tuples([('Science', 'Physics'),
									('Science', 'Chemistry')])

df_multi_level_cols1 = pd.DataFrame([[80, 64], [76, 70]],
									index=['Deepa', 'Balram'],
									columns=multicol1)

print(df_multi_level_cols1)

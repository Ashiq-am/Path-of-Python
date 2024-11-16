# Multi-level with missing values
multicol2 = pd.MultiIndex.from_tuples([('English', 'Literature'),
									('Hindi', 'Language')])

df_multi_level_cols2 = pd.DataFrame([[80, 75], [80, 85]],
									index=['Deepa', 'Balram'],
									columns=multicol2)
df_multi_level_cols2

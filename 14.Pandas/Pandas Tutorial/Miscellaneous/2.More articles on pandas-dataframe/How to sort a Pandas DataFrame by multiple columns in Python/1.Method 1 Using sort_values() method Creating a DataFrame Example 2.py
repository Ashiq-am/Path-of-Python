print('SORTED DATAFRAME')
df.sort_values(by = ['Rank', 'Age'], ascending = [True, False], na_position = 'first')

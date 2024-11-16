print('SORTED DATAFRAME')
df.sort_values(by = ['Name', 'Rank'], axis=0, ascending=[False, True], inplace=False,
			kind='quicksort', na_position='first', ignore_index=True, key=None)

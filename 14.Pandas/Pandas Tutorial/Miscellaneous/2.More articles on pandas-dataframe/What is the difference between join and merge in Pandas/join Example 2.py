joined_df2 = left.reset_index().join(right, on='index', lsuffix='_')
print(joined_df2)

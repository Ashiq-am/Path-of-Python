options = ['Science', 'Commerce']

# selecting rows based on condition
rslt_df = dataframe.loc[dataframe['Stream'].isin(options)]

print('\nResult dataframe :\n',
      rslt_df)

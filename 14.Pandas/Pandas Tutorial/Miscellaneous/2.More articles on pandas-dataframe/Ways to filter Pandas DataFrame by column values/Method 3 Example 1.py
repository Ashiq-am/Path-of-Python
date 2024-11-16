options = ['Commerce', 'Science']

# selecting rows based on condition
rslt_df = dataframe[(dataframe['Age'] == 22) &
                    dataframe['Stream'].isin(options)]

print('\nResult dataframe :\n',
      rslt_df)

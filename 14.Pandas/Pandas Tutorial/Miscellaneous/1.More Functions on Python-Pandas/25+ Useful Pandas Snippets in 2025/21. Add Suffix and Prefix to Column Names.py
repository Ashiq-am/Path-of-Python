df.columns = df.columns + '_suffix'    # Add suffix to all column names.
# or
df.rename(columns=lambda x: 'prefix_' + x, inplace=True)    # Add prefix.

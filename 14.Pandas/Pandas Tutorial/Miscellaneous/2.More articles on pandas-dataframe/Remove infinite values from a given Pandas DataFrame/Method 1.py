# Replacing infinite with nan
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Dropping all the rows with nan values
df.dropna(inplace=True)

# Printing df
df

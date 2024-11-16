# Creating filter
df_filter = df.isin([np.nan, np.inf, -np.inf])

# Masking df with the filter
df = df[~df_filter]

# Dropping rows with nan values
df.dropna(inplace=True)

# Printing df
df

# Changing option to use infinite as nan
pd.set_option('mode.use_inf_as_na', True)

# Dropping all the rows with nan values
df.dropna(inplace=True)

# Printing df
df

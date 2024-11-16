# Changing option to use infinite as nan
with pd.option_context('mode.use_inf_as_na', True):
    # Dropping the rows with nan
    # (or inf) values
    df.dropna(inplace=True)

# Printing df
df

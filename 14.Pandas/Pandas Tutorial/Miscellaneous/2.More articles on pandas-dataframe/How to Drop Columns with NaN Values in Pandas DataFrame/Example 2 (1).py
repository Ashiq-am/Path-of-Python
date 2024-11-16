# Dropping the columns having NaN/NaT values
df = df.dropna(axis=1)

# Resetting the indices using df.reset_index()
df = df.reset_index(drop=True)

df

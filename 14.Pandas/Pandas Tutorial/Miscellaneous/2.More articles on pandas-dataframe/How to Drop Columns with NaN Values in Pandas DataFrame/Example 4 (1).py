# Dropping the columns having NaN/NaT values
# under certain label index using 'subset' attribute
df = df.dropna(subset=[3], axis=1)

# Resetting the indices using df.reset_index()
df = df.reset_index(drop=True)

df

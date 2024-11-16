# Let's find out the current timezone
# of the given dataframe
print(df.index)

# Let's localize the timezone of the
# dataframe index to 'Europe / Berlin'
df = df = df.tz_localize(tz = 'Europe / Berlin')

# Let's find out the current timezone
# of the given dataframe
print(df.index)

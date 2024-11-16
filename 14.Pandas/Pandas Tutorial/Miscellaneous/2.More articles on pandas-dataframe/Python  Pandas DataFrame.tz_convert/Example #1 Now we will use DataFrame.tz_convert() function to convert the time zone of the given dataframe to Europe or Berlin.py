# Let's find out the current timezone
# of the given dataframe
print(df.index)

# Let's convert the timezone of the
# dataframe to 'Europe / Berlin'
df = df.tz_convert(tz = 'Europe / Berlin')

# Let's find out the current timezone
# of the given dataframe
print(df.index)

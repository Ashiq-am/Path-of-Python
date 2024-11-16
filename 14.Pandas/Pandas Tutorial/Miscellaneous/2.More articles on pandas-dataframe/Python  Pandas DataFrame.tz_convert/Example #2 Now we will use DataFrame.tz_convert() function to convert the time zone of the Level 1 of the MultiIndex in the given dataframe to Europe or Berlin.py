# Let's find out the current timezone
# of the Level 1 of the given dataframe
print(df.index[1])

# Let's convert the timezone of the
# level 1 of the dataframe to 'Europe / Berlin'
df = df.tz_convert(tz = 'Europe/Berlin', level = 1)

# Let's find out the current timezone
# of the level 1 of the given dataframe
print(df.index[1])

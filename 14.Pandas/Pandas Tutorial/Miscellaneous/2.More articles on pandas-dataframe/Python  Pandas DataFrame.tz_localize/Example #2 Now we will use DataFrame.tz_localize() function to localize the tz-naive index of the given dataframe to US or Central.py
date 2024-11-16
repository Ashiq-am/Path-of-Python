# Let's find out the current timezone
# of the Level 1 of the given dataframe
print(df.index[1])

# Let's localize the timezone of the
# level 1 of the dataframe to 'US / Central'
df = df.tz_localize(tz = 'US / Central', level = 1)

# Let's find out the current timezone
# of the level 1 of the given dataframe
print(df.index[1])

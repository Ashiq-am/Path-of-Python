df.index = dates
df.index = df.index.tz_localize('US/Pacific')
print(df.index)

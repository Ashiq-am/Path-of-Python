# Create the Index
didx = pd.DatetimeIndex(start ='2014-08-01 10:00', freq ='W',
					periods = 6, tz = 'Europe/Berlin')


# reset the index
sr.set_axis(didx, inplace = True)

# Print the series
print(sr)

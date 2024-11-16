# Use resample function to upsample months
# to days using the mean sales of month
upsampled = data.resample('D').mean()

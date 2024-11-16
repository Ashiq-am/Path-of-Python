# Use resample function to downsample days
# to months using the mean sales of month.
downsampled = data.resample('Q').mean()

# printing the downsampled data.
print(downsampled)

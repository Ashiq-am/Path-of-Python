# use interpolate function with method linear
# to upsample the values of the upsampled days
# linearly
interpolated = upsampled.interpolate(method='linear')

# Printing the linear interpolated values for month 2
print(interpolated['2021-02'])

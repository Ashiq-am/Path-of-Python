# use interpolate function with method polynomial
# This upsamples the values of the remaining
# days with a quadratic function of degree 2.
interpolated = upsampled.interpolate(method='polynomial', order=2)

# Printing the polynomial interpolated value
print(interpolated)

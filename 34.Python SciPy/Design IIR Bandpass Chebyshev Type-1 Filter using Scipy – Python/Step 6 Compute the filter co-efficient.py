# Design digital Chebyshev type-1 filter
# using signal.cheby1 function
z, p = signal.cheby1(N, Ap, wc, 'bandpass')

# Print numerator and denomerator coefficients
# of the filter
print('Numerator Coefficients:', z)
print('Denominator Coefficients:', p)

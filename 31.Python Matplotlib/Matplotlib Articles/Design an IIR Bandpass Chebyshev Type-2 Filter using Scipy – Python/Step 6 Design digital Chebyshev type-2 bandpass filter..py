# Design digital Chebyshev type-2 bandpass
# filter using signal.cheby2 function
z, p = signal.cheby2(N, As, wc, 'bandpass')


# Print numerator and denomerator
# coefficients of the filter
print('Numerator Coefficients:', z)
print('Denominator Coefficients:', p)

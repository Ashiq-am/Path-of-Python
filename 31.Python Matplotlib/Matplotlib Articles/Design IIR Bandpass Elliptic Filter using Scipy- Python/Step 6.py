# Design digital elliptic bandpass filter
# using signal.ellip function
z, p = signal.ellip(N, Ap, As, wc, 'bandpass')


# Print numerator and denomerator
# coefficients of the filter
print('Numerator Coefficients:', z)
print('Denominator Coefficients:', p)

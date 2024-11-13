# Design digital Butterworth band pass
# filter using signal.butter function
z, p = signal.butter(N, wc, 'bandpass')

# Print numerator and denomerator
# coefficients of the filter
print('Numerator Coefficients:', z)
print('Denominator Coefficients:', p)

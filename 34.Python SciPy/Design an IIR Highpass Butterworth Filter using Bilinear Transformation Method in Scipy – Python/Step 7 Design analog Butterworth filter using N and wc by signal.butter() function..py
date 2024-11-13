# Design analog Butterworth filter using N and
# wc by signal.butter function
b, a = signal.butter(N, wc, 'high', analog=True)

# Perform bilinear Transformation
z, p = signal.bilinear(b, a, fs=Fs)

# Print numerator and denomerator coefficients
# of the filter
print('Numerator Coefficients:', z)
print('Denominator Coefficients:', p)

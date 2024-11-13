# Design analog Butterworth filter using signal.butter function

b, a = signal.butter(N, wc, 'low', analog='True')
# Perform bilinear Transformation

z, p = signal.bilinear(b, a, fs=Fs)

# Print numerator and denomerator coefficients of the filter
print('Numerator Coefficients:', z)
print('Denominator Coefficients:', p)

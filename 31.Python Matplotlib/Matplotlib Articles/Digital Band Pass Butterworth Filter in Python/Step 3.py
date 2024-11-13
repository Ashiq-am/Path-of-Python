# Conversion to prewrapped analog
# frequency
omega_p = convertX(f_sample, f_pass)
omega_s = convertX(f_sample, f_stop)

# Design of Filter using signal.buttord
# function
N, Wn = signal.buttord(omega_p, omega_s,
                       g_pass, g_stop,
                       analog=True)

# Printing the values of order & cut-off frequency
# N is the order
print("Order of the Filter=", N)

# Wn is the cut-off freq of the filter
print("Cut-off frequency= {:} rad/s ".format(Wn))

# Conversion in Z-domain

# b is the numerator of the filter & a is
# the denominator
b, a = signal.butter(N, Wn, 'bandpass', True)
z, p = signal.bilinear(b, a, fs)

# w is the freq in z-domain & h is the
# magnitude in z-domain
w, h = signal.freqz(z, p, 512)

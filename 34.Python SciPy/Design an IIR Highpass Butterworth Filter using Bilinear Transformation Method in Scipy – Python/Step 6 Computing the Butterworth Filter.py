# Compute Butterworth filter order and cutoff frequency
N, wc = signal.buttord(Omega_p, Omega_s, Ap, As, analog=True)

# Print the values of order and cut-off frequency
print('Order of the filter=', N)
print('Cut-off frequency=', wc)

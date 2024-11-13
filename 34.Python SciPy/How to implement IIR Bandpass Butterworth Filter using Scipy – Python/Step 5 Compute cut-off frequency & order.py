# Compute order of the digital Butterworth filter using signal.buttord
N, wc = signal.buttord(wp, ws, Ap, As, analog=True)
# Print the order of the filter and cutoff frequencies
print('Order of the filter=', N)
print('Cut-off frequency=', wc)

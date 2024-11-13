# Compute order of the Chebyshev type-1 filter using signal.cheb1ord
N, wc = signal.cheb1ord(wp, ws, Ap, As)

# Print the order of the filter and cutoff frequencies
print('Order of the filter=', N)
print('Cut-off frequency=', wc)

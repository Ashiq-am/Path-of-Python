# Compute order of the Chebyshev type-2
# digital filter using signal.cheb2ord
N, wc = signal.cheb2ord(wp, ws, Ap, As)

# Print the order of the filter
# and cutoff frequencies
print('Order of the filter=', N)
print('Cut-off frequency=', wc)

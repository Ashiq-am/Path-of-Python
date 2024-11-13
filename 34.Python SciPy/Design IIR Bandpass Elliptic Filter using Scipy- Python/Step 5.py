# Compute order of the elliptic filter
# using signal.ellipord
N, wc = signal.ellipord(wp, ws, Ap, As)

# Print the order of the filter and
# cutoff frequencies
print('Order of the filter=', N)
print('Cut-off frequency=', wc)

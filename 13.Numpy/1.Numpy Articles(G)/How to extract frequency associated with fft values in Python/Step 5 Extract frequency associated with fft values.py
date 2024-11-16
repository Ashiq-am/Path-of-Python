# extract frequencies associated with FFT values
for coef, freq in zip(w, freqs):
	if coef:
		print('{c:>6} * exp(2 pi i t * {f})'.format(c=coef,
													f=freq))

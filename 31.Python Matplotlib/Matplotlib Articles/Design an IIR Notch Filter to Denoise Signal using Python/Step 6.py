# Generate the signal containing f1 and f2
noisySignal = np.sin(2*np.pi*15*n) + np.sin(2*np.pi*50*n) + \
	np.random.normal(0, .1, 1000)*0.03

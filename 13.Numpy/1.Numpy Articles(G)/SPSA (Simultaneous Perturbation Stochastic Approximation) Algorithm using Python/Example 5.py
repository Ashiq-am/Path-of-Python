def initialize_hyperparameters(alpha, lossFunction, w0, N_iterations):

	c = 1e-2 # a small number

	# A is <= 10% of the number of iterations
	A = N_iterations*0.1

	# order of magnitude of first gradients
	magnitude_g0 = np.abs(grad(lossFunction, w0, c).mean())

	# the number 2 in the front is an estimative of
	# the initial changes of the parameters,
	# different changes might need other choices
	a = 2*((A+1)**alpha)/magnitude_g0

	return a, A, c

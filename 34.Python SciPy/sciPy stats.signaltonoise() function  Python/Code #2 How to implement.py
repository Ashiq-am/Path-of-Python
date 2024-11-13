def signaltonoise(a, axis, ddof):
	a = np.asanyarray(a)
	m = a.mean(axis)
	sd = a.std(axis = axis, ddof = ddof)
	return np.where(sd == 0, 0, m / sd)

print ("\nsignaltonoise ratio for arr1 : ",
	signaltonoise(arr1, axis = 0, ddof = 0))

print ("\nsignaltonoise ratio for arr1 : ",
	signaltonoise(arr1, axis = 1, ddof = 0))

print ("\nsignaltonoise ratio for arr2 : ",
	signaltonoise(arr2, axis = 0, ddof = 0))

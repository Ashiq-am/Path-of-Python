a = timeit('numpy.clip(arr2, -5, 5, arr3)',
	'from __main__ import b, c, numpy', number = 1000)

print ("\nTime for NumPy clip program : ", a)

b = timeit('sample.clip(arr2, -5, 5, arr3)',
		'from __main__ import b, c, sample', number = 1000)

print ("\nTime for our program : ", b)

def polynomial(a, x):

	N = len(a)
	S = 0
	for k in range(N):
		S += a[k]*x**k
	return S

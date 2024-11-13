def factorial( n) :
	M = 1000000007
	f = 1

	for i in range(1, n + 1):
		f = f * i # WRONG APPROACH as
				# f may exceed (2^64 - 1)

	return f % M

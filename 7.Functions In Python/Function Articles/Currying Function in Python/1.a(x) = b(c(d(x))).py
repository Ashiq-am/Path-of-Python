def change(b, c, d):
	def a(x):
		return b(c(d(x)))
	return a

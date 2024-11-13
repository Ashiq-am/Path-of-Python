# explicit function to convert
# edge frequencies


def convertX(f_sample, f):
	w = []

	for i in range(len(f)):
		b = 2*((f[i]/2) / (f_sample/2))
		w.append(b)

	omega_mine = []

	for i in range(len(w)):
		c = (2/Td)*np.tan(w[i]/2)
		omega_mine.append(c)

	return omega_mine

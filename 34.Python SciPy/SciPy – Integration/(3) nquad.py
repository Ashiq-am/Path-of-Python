from scipy.integrate import nquad


def f(x, y, z):
	return x*y*z


I = nquad(f, [[0, 1], [0, 5], [0, 5]])
print(I)

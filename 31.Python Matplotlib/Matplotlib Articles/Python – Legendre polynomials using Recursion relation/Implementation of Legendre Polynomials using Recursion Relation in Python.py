import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Defining Legendre polynomials using
# Recursion relation
def legendre(n, x):
	if n == 0:
		return 1
	elif n == 1:
		return x
	else:
		return ((2*n - 1)*x*legendre(n-1, x)
				- (n - 1)*legendre(n-2, x))/n


x = 0.5

# Run a loop to find the values from
# P0 to P4
for n in range(5):
	print(f"P_{n}({x}) = {legendre(n, x)}")


x = np.linspace(-2, 2, 100)

# plot the graph for values from
# P1 to P4
for i in range(1, 5):
	plt.plot(x, legendre(i, x), label=i)

plt.legend(loc="best")
plt.xlabel("x")
plt.ylabel("pn")
plt.show()

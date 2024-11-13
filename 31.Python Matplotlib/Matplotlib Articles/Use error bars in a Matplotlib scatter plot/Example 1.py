import matplotlib.pyplot as plt

a = [1, 3, 5, 7]
b = [11, -2, 4, 19]
plt.scatter(a, b)

c = [1, 3, 2, 1]

plt.errorbar(a, b, yerr=c, fmt="o")
plt.show()

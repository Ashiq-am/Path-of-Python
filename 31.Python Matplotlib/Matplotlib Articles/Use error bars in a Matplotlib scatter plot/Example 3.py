import matplotlib.pyplot as plt

a = [1, 3, 5, 7]
b = [11, -2, 4, 19]
plt.scatter(a, b)


c = [1, 3, 2, 1]
d = [1, 3, 2, 1]

# you can use color ="r" for red or skip to default as blue
plt.errorbar(a, b, xerr=c, yerr=d, fmt="o", color="r")

plt.show()

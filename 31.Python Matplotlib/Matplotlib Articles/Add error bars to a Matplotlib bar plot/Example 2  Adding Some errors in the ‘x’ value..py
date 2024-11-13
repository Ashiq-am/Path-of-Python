# importing matplotlib
import matplotlib.pyplot as plt

# making a simple plot
a = [1, 3, 5, 7]
b = [11, 2, 4, 19]

# Plot scatter here
plt.bar(a, b)

c = [1, 3, 2, 1]

plt.errorbar(a, b, xerr=c, fmt="o", color="r")

plt.show()

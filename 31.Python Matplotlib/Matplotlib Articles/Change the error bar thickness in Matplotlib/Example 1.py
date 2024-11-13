# importing necessary libraries
import matplotlib.pyplot as plt

# example data
x = np.arange(3, 5, 0.5)
y = np.arange(9, 11, 0.5)

# ploting with default thickness of bar
plt.title("1. Without changing thickness")
plt.errorbar(x, y, xerr=0.2, yerr=0.6, fmt='o')
plt.show()

# ploting with changed thickness of bar
plt.title("1. With changed thickness of bar")

# change elinwidth to change the thickness of bar
plt.errorbar(x, y, xerr=0.2, yerr=0.6, fmt='o', elinewidth=4)
plt.show()

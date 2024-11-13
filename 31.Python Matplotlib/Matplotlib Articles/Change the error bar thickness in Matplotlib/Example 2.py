# importing necessary libraries
import matplotlib.pyplot as plt

# example data
x = np.arange(1, 3, 0.5)
y = np.log(x)

# ploting with default thickness of bar
plt.title("2. Without changing thickness")
plt.errorbar(x, y, xerr=0.2, yerr=0.4, fmt='o', ecolor='black', capsize=5)
plt.show()

# ploting with changed thickness of bar
# change elinwidth to change the thickness of bar
plt.title("2. With changed thickness of bar")
plt.errorbar(x, y, xerr=0.2, yerr=0.4, fmt='o', elinewidth=4,
			ecolor='black', capsize=5, capthick=3)

plt.show()

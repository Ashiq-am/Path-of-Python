import matplotlib.pyplot as plt

x_values = [0, 1, 2, 3, 4, 5]
y_values = [8, 4, 9, 1, 0, 5]


x_error = [0, 0.3, 1, 0.2, 0.75, 2]
y_error = [0.3, 0.3, 2, 0.5, 0.7, 0.6]

plt.errorbar(x_values, y_values, xerr=x_error, yerr=y_error,
			fmt='D', markersize=8, capsize=3, color="r")

plt.show()

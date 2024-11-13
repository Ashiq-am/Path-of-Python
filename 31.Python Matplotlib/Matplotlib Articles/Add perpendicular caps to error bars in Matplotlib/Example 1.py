import matplotlib.pyplot as plt

x_values = [5, 4, 3, 2, 1]
y_values = [8, 4, 9, 1, 0]

y_error = [0, 0.3, 1, 0.2, 0.75]

plt.errorbar(x_values, y_values, yerr=y_error,
			fmt='o', markersize=8, capsize=10)

plt.show()

import matplotlib.pyplot as plt

x_values = [0, 1, 2, 3, 4, 5]
y_values = [8, 4, 9, 1, 0, 5]

plt.plot(x_values, y_values)
x_error = [0, 0.3, 1, 0.2, 0.75, 2]

plt.errorbar(x_values, y_values, xerr=x_error,
			fmt='o', markersize=8, capsize=6, color="r")

plt.show()

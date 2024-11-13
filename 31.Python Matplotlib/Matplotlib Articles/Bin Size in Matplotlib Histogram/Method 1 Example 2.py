import matplotlib.pyplot as plt

values = [87, 53, 66, 61, 67, 68, 62,
		110, 104, 61, 111, 123, 117,
		119, 116, 104, 92, 111, 90,
		103, 81, 80, 101, 51, 79, 107,
		110, 129, 145, 139, 110]

plt.hist(values, bins=7, edgecolor="yellow", color="green")
plt.show()

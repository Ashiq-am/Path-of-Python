import matplotlib.pyplot as plt

data = [87, 53, 66, 61, 67, 68, 62, 110,
		104, 61, 111, 123, 117, 119, 116,
		104, 92, 111, 90, 103, 81, 80, 101,
		51, 79, 107, 110, 129, 145, 128,
		132, 135, 131, 126, 139, 110]

binwidth = 8
plt.hist(data, bins=range(min(data), max(data) + binwidth, binwidth),
		edgecolor="yellow", color="brown")

plt.show()

import matplotlib.pyplot as plt

data = [189, 185, 195, 149, 189, 147,
		154, 174, 169, 195, 159, 192,
		155, 191, 153, 157, 140, 144,
		172, 157, 181, 182, 166, 167]

plt.hist(data, bins=[140, 150, 160, 175, 185, 200],
		edgecolor="yellow", color="grey")

plt.show()

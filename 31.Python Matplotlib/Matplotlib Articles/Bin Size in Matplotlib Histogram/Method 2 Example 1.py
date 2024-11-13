import matplotlib.pyplot as plt

marks = [1, 2, 3, 2, 1, 2, 3, 2,
		1, 4, 5, 4, 3, 2, 5, 4,
		5, 4, 5, 3, 2, 1, 5]

plt.hist(marks, bins=[1, 2, 3, 4, 5], edgecolor="black")
plt.show()

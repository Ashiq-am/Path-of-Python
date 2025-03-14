# Importing libraries
import matplotlib.pyplot as plt

# Preparing dataset
x = [x for x in range(10)]
y = [5, 2, 4, 8, 5, 6, 8, 7, 1, 3]
text = ["first", "second", "third", "fourth", "fifth",
		"sixth", "seventh", "eighth", "ninth", "tenth"]

# plotting scatter plot
plt.scatter(x, y)

# Loop for annotation of all points
for i in range(len(x)):
	plt.annotate(text[i], (x[i], y[i] + 0.2))

# adjusting the scale of the axes
plt.xlim((-1, 10))
plt.ylim((0, 10))
plt.show()

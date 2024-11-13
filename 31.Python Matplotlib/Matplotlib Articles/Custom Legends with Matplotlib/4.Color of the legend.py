# importing library
import matplotlib.pyplot as plt

# plotting values
a = [1, 2, 3, 4]
b = [1, 4, 9, 16]

# PLotting using matplotlib
plt.plot(a, label="label1")
plt.plot(b, label="label2")

# Creating legend
# Adding color to the legend
plt.legend(labelcolor='white', facecolor='black',
		edgecolor='red', fontsize='xx-large')

# Importing libraries
import matplotlib.pyplot as plt

# Preparing dataset
x = [x for x in range(10)]
y = [5, 4, 4, 8, 5, 6, 8, 7, 1, 3]

# plotting scatter plot
plt.scatter(x, y)

# annotation of the third point
plt.text(2,4.2,"third")
plt.show()

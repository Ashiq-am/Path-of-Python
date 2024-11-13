import matplotlib.pyplot as plt

values = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8]

# Adjust the bar widths here
plt.hist(values)

plt.ylabel("Quantity")
plt.xlabel("Value")
plt.show()

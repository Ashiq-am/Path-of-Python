# Importing the Library

import matplotlib.pyplot as plt
# Defining X-axis and Y-axis data Points
x = [0, 1, 2, 3, 4, 5, 6, 8]
y = [1, 5, 2, 8, 3, 5, 2, 7]

# Defining the Width and height of the Figure
plt.figure(figsize=(8, 7))
plt.plot(x, y)
plt.show()

# importing the library
import numpy as np
import matplotlib.pyplot as plt

# Initializing variable
y = np.ones(10)

# Calculating result
res = np.geomspace(10, 1000, 10, endpoint = True)

# Printing the result
print(res)

# Plotting the graph
plt.scatter(res, y, color = 'green')
plt.title('logarithmically spaced numbers')
plt.show()

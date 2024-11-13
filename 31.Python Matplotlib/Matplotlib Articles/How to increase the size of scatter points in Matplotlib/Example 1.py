import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [8, 7, 6, 4, 5, 6, 7, 8, 9, 10]

plt.xticks(np.arange(11))
plt.yticks(np.arange(11))

plt.scatter(x, y, s=500, c='g')

plt.title("Scatter Plot", fontsize=25)

plt.xlabel('x-axis', fontsize=18)
plt.ylabel('y-axis', fontsize=18)

plt.show()

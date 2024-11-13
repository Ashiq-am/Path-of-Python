import matplotlib.pyplot as plt
import numpy as np

X, Y = np.loadtxt('GFG.txt', delimiter=',', unpack=True)

plt.bar(X, Y)
plt.title('Line Graph using NUMPY')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

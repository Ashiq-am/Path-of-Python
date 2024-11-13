import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)

# Move labels from bottom to top
ax.tick_params(axis='x', which='both', labelbottom=False, bottom=False, top=False, labeltop=True)
plt.show()

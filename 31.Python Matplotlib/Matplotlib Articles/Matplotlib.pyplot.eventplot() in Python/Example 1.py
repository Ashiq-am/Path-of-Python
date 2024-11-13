import numpy as np
import matplotlib.pyplot as plt

positions = np.array([2, 4, 6])[:,np.newaxis]
offsets = [2,4,6]

plt.eventplot(positions, lineoffsets=offsets)
plt.show()

# importing packages
import matplotlib.pyplot as plt
import numpy as np

# making subplots objects
fig, ax = plt.subplots(2, 2)

# draw graph
ax[0][0].plot(np.random.randint(0, 5, 5), np.random.randint(0, 5, 5))
ax[0][1].plot(np.random.randint(0, 5, 5), np.random.randint(0, 5, 5))
ax[1][0].plot(np.random.randint(0, 5, 5), np.random.randint(0, 5, 5))
ax[1][1].plot(np.random.randint(0, 5, 5), np.random.randint(0, 5, 5))

plt.show()

# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
import numpy as np

# create test data
np.random.seed(10 ** 7)
data = [sorted(np.random.normal(0, std, 100))
        for std in range(1, 5)]

fig, ax1 = plt.subplots()
val = ax1.violinplot(data)
ax1.set_ylabel('Result')
ax1.set_xlabel('Domain Name')

for i in val['bodies']:
    i.set_facecolor('green')
    Artist.set_alpha(i, 0.5)

fig.suptitle('matplotlib.artist.Artist.set_alpha()\
function Example', fontweight="bold")

plt.show()

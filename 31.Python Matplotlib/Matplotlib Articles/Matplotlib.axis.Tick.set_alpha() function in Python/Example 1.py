# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import numpy as np

# create test data
np.random.seed(10 ** 7)
data = [sorted(np.random.normal(0, std, 100))
        for std in range(1, 4)]

fig, ax1 = plt.subplots()
val = ax1.violinplot(data)

for i in val['bodies']:
    i.set_facecolor('purple')
    Tick.set_alpha(i, 0.4)

fig.suptitle('matplotlib.axis.Tick.set_alpha() \
function Example', fontweight="bold")

plt.show()

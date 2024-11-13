# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

np.random.seed(10 ** 7)
data = np.random.lognormal(size=(10, 4),
                           mean=4.5,
                           sigma=4.75)

labels = ['G1', 'G2', 'G3', 'G4']

result = cbook.boxplot_stats(data,
                             labels=labels,
                             bootstrap=1000)

for n in range(len(result)):
    result[n]['med'] = np.median(data)
    result[n]['mean'] *= 0.1

fig, axes1 = plt.subplots()
axes1.bxp(result)

axes1.text(2, 30000,
           "Value return : "
           + str(Axis.pickable(axes1)),
           fontweight="bold")

fig.suptitle('matplotlib.axis.Axis.pickable() \
function Example\n', fontweight="bold")

plt.show()

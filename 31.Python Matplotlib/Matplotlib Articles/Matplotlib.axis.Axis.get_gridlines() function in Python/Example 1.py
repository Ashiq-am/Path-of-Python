# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt
import random

fig, ax2 = plt.subplots()
x = []

for i in range(1, 11):
    j = random.randint(1, 10)
    x.append(i * j)
ax2.plot(x)

print("Value of get_gridlines() :")
for i in ax2.xaxis.get_gridlines():
    print(i)

fig.suptitle("Matplotlib.axis.Axis.get_gridlines()\
Function Example", fontsize=12, fontweight='bold')

plt.show()

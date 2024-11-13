import numpy as np
import matplotlib.pyplot as plt
from random import randint

# Creating 3 empty lists
l1 = []
l2 = []
l3 = []

# Filling the lists with random value
for i in range(100):
    n = randint(1, 100)
    l1.append(n)

for i in range(100):
    n = randint(1, 100)
    l2.append(n)

for i in range(100):
    n = randint(1, 100)
    l3.append(n)

random_collection = [l1, l2, l3]

# Create a figure instance
fig = plt.figure()

# Create an axes instance
ax = fig.gca()

# Create the violinplot
violinplot = ax.violinplot(random_collection)
plt.show()

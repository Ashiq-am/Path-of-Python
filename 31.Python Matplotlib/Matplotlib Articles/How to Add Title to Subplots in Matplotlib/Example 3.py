# importing packages
import numpy as np
import matplotlib.pyplot as plt

# create data
x = np.array([1, 2, 3, 4, 5])

# making subplots
fig, ax = plt.subplots(2, 2)

# set data with subplots and plot
title = ["Linear", "Double", "Square", "Cube"]
y = [x, x * 2, x * x, x * x * x]

for i in range(4):
    # subplots
    plt.subplot(2, 2, i + 1)

    # ploting (x,y)
    plt.plot(x, y[i])

    # set the title to subplots
    plt.gca().set_title(title[i])

# set spacing
fig.tight_layout()
plt.show()

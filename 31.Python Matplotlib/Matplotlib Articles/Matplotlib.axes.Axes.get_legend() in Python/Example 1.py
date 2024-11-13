# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot([1, 6, 3, 8, 34, 13, 56, 67], color="green")

x = ax.get_legend()
text = "Legend is present"
if x == None:
    text = "No legend present"

ax.text(2.5, 60, text, fontweight="bold")
fig.suptitle('matplotlib.axes.Axes.get_legend() function\
Example\n', fontweight="bold")
fig.canvas.draw()
plt.show()

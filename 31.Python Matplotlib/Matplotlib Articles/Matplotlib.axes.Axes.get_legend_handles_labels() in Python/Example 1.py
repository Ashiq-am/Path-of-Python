# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot([1, 6, 3, 8, 34, 13, 56, 67], color="green")

h, l = ax.get_legend_handles_labels()
# print(h, l)
text = "Legend is present"
if h == []:
    text = "No legend present"
else:
    text += "and labels are : " + str(l)

ax.text(2.5, 60, text, fontweight="bold")
fig.suptitle('matplotlib.axes.Axes.get_legend_handles_labels()\
function Example\n', fontweight="bold")
fig.canvas.draw()
plt.show()

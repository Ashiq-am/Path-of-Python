# ImpleIn Reviewtation of matplotlib function
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
ax1.set_xscale("log")
ax1.set_yscale("log")
ax1.set_adjustable("datalim")

ax1.plot([1, 3, 34, 4, 46, 3, 7, 45, 10],
         [1, 9, 27, 8, 29, 84, 78, 19, 48],
         "o-", color="green")

ax1.set_xlim(1e-1, 1e2)
ax1.set_ylim(1, 1e2)

w = ax1.has_data()

print("Value Return by has_data() :", w)

fig.suptitle('matplotlib.axes.Axes.has_data()\
function Example\n\n', fontweight="bold")

fig.canvas.draw()

plt.show()

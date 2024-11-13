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

w = ax1.get_default_bbox_extra_artists()

print("Value Return by get_default_bbox_extra_artists() :")

for i in w:
    print(i)

fig.suptitle('matplotlib.axes.Axes.get_default_bbox_extra_artists()\
function Example\n\n', fontweight="bold")

fig.canvas.draw()

plt.show()

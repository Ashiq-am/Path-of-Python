import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3])

# Hide ticks and labels
a = plt.gca()
xax = a.axes.get_xaxis()
xax.set_visible(False)
yax = a.axes.get_yaxis()
yax.set_visible(False)
plt.show()

import matplotlib.pyplot as plt

x = [5, 8, 15, 20, 30]
y = [15, 10, 8, 20, 15]
plt.plot(x, y, color='g', linewidth=5)

# getting current axes
a = plt.gca()

# set visibility of x-axis as False
xax = a.axes.get_xaxis()
xax = xax.set_visible(False)

# set visibility of y-axis as False
yax = a.axes.get_yaxis()
yax = yax.set_visible(False)

plt.show()

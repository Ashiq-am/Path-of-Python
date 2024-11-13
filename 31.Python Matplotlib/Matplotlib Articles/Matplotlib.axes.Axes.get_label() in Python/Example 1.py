# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = [0, 1]
y = [1, 1]
line, = ax.plot(x, y)
ax.legend(("Line_1", ))

ax.text(0.2, 1.02, "Value Return by get_label(): " + str(line.get_label()))


fig.suptitle('matplotlib.axes.Axes.get_label() function Example\n\n', fontweight ="bold")

plt.show()

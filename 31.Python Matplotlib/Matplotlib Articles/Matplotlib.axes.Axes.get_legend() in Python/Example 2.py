# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, (ax, ax1) = plt.subplots(1, 2)
# axes1
line1, = ax.plot([1, 2, 3], label ="Line 1",
				color ="black", linewidth = 4,
				linestyle =':')

line2, = ax.plot([3, 2, 1], label ="Line 2",
				color ="green",
				linewidth = 4)

first_legend = ax.legend(handles =[line1],
						loc ='upper center')

ax.add_artist(first_legend)

ax.legend(handles =[line2], loc ='lower center')
ax.set_title("Without get_legend function")
# axes1
line1, = ax1.plot([1, 2, 3], label ="Line 1",
				color ="black", linewidth = 4,
				linestyle =':')
line2, = ax1.plot([3, 2, 1], label ="Line 2",
				color ="green",
				linewidth = 4)

first_legend = ax1.legend(handles =[line1],
						loc ='upper center')

ax1.add_artist(first_legend)

ax1.legend(handles =[line2],
		loc ='lower center')
ax1.get_legend().set_visible(False)
ax1.set_title("Using get_legend function")
fig.suptitle('matplotlib.axes.Axes.get_legend() function Example\n', fontweight ="bold")

plt.show()

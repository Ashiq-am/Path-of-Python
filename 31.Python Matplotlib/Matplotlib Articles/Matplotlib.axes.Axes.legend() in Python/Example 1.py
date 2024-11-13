# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

line1, = ax.plot([1, 2, 3],
				label ="Line 1",
				color ="black",
				linewidth = 4,
				linestyle =':')

line2, = ax.plot([3, 2, 1],
				label ="Line 2",
				color ="green",
				linewidth = 4)


first_legend = ax.legend(handles =[line1],
						loc ='upper center')

ax.add_artist(first_legend)

ax.legend(handles =[line2], loc ='lower center')

fig.suptitle('matplotlib.axes.Axes.legend() function Example\n', fontweight ="bold")

plt.show()

#import required library
import matplotlib.pyplot as plt

# specifing the subplot
fig, axes = plt.subplots(nrows = 4,
						ncols = 4,
						figsize = (10,10))

# Or equivalently,
# "plt.tight_layout()"
fig.tight_layout()

# subplot 1
plt.subplot(2, 2, 1)
x2 = [0.1, 10, -30]
y2 = [40, -10, 45]

# plotting the given graph
plt.semilogx(x2, y2,
			color = "blue",
			linewidth = 4)
# set the title
plt.title("USING LINE")

# set y axis label
plt.ylabel('-----------y-----------')

# set x axis label
plt.xlabel('-----------x-----------')

# plot with grid
plt.grid(True)


# subplot 2
plt.subplot(2, 2, 2)
x2 = [0.1, 10, -30]
y2 = [40, -10, 45]

# plotting the given graph
plt.semilogx(x2, y2,
			'g^',
			markersize = 20,
			color = "black")
# set the title
plt.title("USING SYMBOL")

# set y axis label
plt.ylabel('-----------y-----------')

# set x axis label
plt.xlabel('-----------x-----------')

# plot with grid
plt.grid(True)

# subplot 3
plt.subplot(2, 2, 3)
x2 = [0.1, 10, -30]
y2 = [40, -10 ,45]

# plotting the given graph
plt.semilogx(x2, y2,
			nonposx = "clip",
			color = "red",
			linewidth = 4)
# set the title
plt.title("CLIPPED")

# set y axis label
plt.ylabel('-----------y-----------')

# set x axis label
plt.xlabel('-----------x-----------')

# plot with grid
plt.grid(True)

# subplot 4
plt.subplot(2, 2, 4)
x2 = [0.1, 10, -30]
y2 = [40, -10, 45]

# plotting the given graph
plt.semilogx(x2, y2,
			nonposx = "mask",
			color = "green",
			linewidth = 4)

# set the title
plt.title("MASKED")

# set y axis label
plt.ylabel('-----------y-----------')

# set x axis label
plt.xlabel('-----------x-----------')

# plot with grid
plt.grid(True)

# show the plot
plt.show()

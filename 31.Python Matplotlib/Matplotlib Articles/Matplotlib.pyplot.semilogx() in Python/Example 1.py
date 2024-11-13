#import required library
import matplotlib.pyplot as plt

# defining the values
# at X and Y axis
x = [1, 2, 3,
	4, 5, 6]
y = [100, 200, 300,
	400, 500, 600]

# plotting the given graph
plt.semilogx(x, y, marker = ".",
			markersize = 15,
			color = "green")
# plot with grid
plt.grid(True)

# show the plot
plt.show()

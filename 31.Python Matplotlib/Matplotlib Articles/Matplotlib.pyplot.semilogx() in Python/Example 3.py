#import required library
import matplotlib.pyplot as plt

# defining the values at X and Y axis
x = [-10, 30, 0, 20,
	-50, 25, 29, -3
	, 23, 25, 29, 31]
y = [-3, 30, -10, 0,
	-40, 3, 8, 0,
	-24, 40, 43, 25]

# plotting the graph
plt.semilogx(x,y,'g^', color = "red")

# plot with grid
plt.grid(True)

# set y axis label
plt.ylabel('---y---')

# set x axis label
plt.xlabel('---x---')

# show the plot
plt.show()

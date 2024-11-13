# Importing matplotlib.pyplot as plt
import matplotlib.pyplot as plt


# Initialising values of x and y
x =[0, 5, 10, 15, 20]
y =[1, 3, 5, 6, 9]

# Plotting the graph
plt.plot(x, y)

# Drawing red vertical line at
# x = 2.5 starting at half the
#length of y axis(ymin = 0.5) and
#continuing till the end(ymax = 1)
# And setting the color of line to red
plt.axvline(x = 2.5, ymin = 0.5, ymax = 1,
			color ='red')

plt.show()

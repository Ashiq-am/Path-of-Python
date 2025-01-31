# importing matplotlib.pyplot module
import matplotlib.pyplot as plt

# values of x and y axes
x = [6, 12, 18,
	24, 30, 36,
	42, 48, 54,
	60]

y = [1, 4, 3,
	2, 7, 6,
	9, 8, 10,
	5]

# plotting the graph
plt.plot(x, y)

# labelling axes
plt.xlabel('x')
plt.ylabel('y')

# Adding title to the graph
# with left horizontal alignment
# and font size 12.
plt.suptitle('This is the figure title',
			ha = 'left',
			fontsize = 12)

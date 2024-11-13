# importing libraries
import matplotlib.pyplot as plt

plt.locator_params(nbins = 10)

# defining the plot
plt.plot([1, 2, 3, 5, 7],
		[2, 3, 9, 15, 16],
		'ro-', color ='red')

# printing the plot
plt.show()

# import matplotlib
import matplotlib.pyplot as plt

# import numpy module
import numpy

# create array 1 for first line
firstarray1 = [1, 3, 5, 7, 9, 11, 13, 15, 17]

# create array 2 for first line
secondarray1 = [23, 45, 2, 56, 78, 45, 67, 23, 11]

# create array 1 for second line
firstarray2 = [2, 4, 6, 8, 10, 45, 32, 11, 78]

# create array 2 for second line
secondarray2 = [11, 34, 56, 43, 56]

# plot the line1 with sin function
plt.plot(firstarray1, numpy.sin(firstarray1),
		linestyle='dotted', label='line1',
		linewidth=6, color="green")

# plot the line2 with cos function
plt.plot(firstarray2, numpy.cos(secondarray1),
		linestyle='dotted', label='line2', linewidth=8)

plt.legend()

# display
plt.show()

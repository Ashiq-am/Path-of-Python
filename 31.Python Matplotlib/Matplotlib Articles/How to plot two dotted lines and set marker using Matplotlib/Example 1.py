# import matplotlib
import matplotlib.pyplot as plt

# create array 1 for first line
firstarray1 = [1, 3, 5, 7, 9, 11, 23, 45, 67, 89]

# create array 2 for first line
secondarray1 = [23, 45, 2, 56, 78, 11, 22, 33, 44, 45]

# create array 1 for second line
firstarray2 = [2, 4, 6, 8, 10, 11, 22, 33, 44]

# create array 2 for second line
secondarray2 = [11, 34, 56, 43, 56, 11, 22, 33, 44]

# plot the line1
plt.plot(firstarray1, secondarray1, linestyle='dotted',
		label='line1', linewidth=6, color="pink")

# plot the line2
plt.plot(firstarray2, secondarray2, linestyle='dotted',
		label='line2', linewidth=8)

plt.legend()

# display
plt.show()

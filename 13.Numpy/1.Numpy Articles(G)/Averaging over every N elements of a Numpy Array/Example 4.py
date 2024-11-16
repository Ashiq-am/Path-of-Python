import numpy as np
# converting list to numpy array
givenArray = np.array([[60, 50, 40], [30, 20, 10], [90, 80,70],
					[120, 110, 100], [150, 140, 130]])

# here we will calculate average over
# every 5 elements
n = 5

# calculates the average
avgResult1 = givenArray.mean(axis=0)

print("Given array:")
print(givenArray, "\n")

print("Dimensions of given array:", givenArray.shape, "\n")

print("Averaging over every ", n, " elements of a numpy array:")
print(avgResult1)

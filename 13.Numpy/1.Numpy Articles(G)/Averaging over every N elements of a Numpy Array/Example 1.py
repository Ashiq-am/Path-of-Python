import numpy as np

# converting list to numpy array
givenArray = np.array([6, 5, 4, 3, 2, 1, 9,
					8, 7, 12, 11, 10, 15,
					14, 13])

# here we took 3 as our input
n = 3

# calculates the average
avgResult = np.average(givenArray.reshape(-1, n), axis=1)

print("Given array:")
print(givenArray)

print("Averaging over every ", n, " elements of a numpy array:")
print(avgResult)

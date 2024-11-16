# Python code to find mean of
# every numpy array in list

# Importing module
import numpy as np

# List Initialization
Input = [np.array([11, 12, 13]),
		np.array([14, 15, 16]),
		np.array([17, 18, 19])]

# Output list initialization
Output = []

# using np.mean()
for i in range(len(Input)):
    Output.append(np.average(Input[i]))

# Printing output
print(Output)

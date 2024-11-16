# importing the module
import numpy as np

# create the arrays
x1 = ['Hello', 'to', 'all']
x2 = ['Geeks', 'for', 'Geeks']
print("The arrays are : ")
print(x1)
print(x2)

# using the char.add() method
result = np.char.add(x1, x2)
print("\nThe concatenated array is :")
print(result)

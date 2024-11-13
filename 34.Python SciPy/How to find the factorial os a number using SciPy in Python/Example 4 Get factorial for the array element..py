# importing module
import numpy as np
from scipy.special import factorial

# creating list
list = [6, 3, 4, 5]

# creating NumPy Array
arr = np.array(list)

# computing factorial and display
print("Factorial value in float : ", factorial(arr, exact=0))

print("Factorial value in Integer : ", factorial(arr, exact=1))

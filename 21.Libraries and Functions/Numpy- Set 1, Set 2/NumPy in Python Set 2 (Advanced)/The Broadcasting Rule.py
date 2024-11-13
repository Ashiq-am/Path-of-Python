import numpy as np

a = np.array([1.0, 2.0, 3.0])

# Example 1
b = 2.0
print(a * b)

# Example 2
c = [2.0, 2.0, 2.0]
print(a * c)






'''In above example, the scalar b is stretched to become an array of with the same shape as a so the shapes 
are compatible for element-by-element multiplication.

Now, let us see an example where both arrays get stretched.'''






import numpy as np

a = np.array([0.0, 10.0, 20.0, 30.0])
b = np.array([0.0, 1.0, 2.0])

print(a[:, np.newaxis] + b)

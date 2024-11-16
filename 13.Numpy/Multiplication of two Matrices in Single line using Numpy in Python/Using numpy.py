# same result will be obtained when we use @ operator
# as shown below(only in python >3.5)
import numpy as np

# input two matrices
mat1 = ([1, 6, 5],[3 ,4, 8],[2, 12, 3])
mat2 = ([3, 4, 6],[5, 6, 7],[6,56, 7])

# This will return matrix product of two array
res = mat1 @ mat2

# print resulted matrix
print(res)









'''In the above example we have used dot product and in mathematics the dot product is an algebraic 
operation that takes two vectors of equal size and returns a single number. The result is calculated by 
multiplying corresponding entries and adding up those products.'''
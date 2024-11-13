# Python3 code to demonstrate
# Non-Repeating value Summation in Matrix
# chain() + set() + sum()
from itertools import chain

# initializing matrix
test_matrix = [[1, 3, 1], [4, 5, 3], [1, 2, 4]]

# printing the original matrix
print ("The original matrix is : " + str(test_matrix))

# using chain() + set() + sum()
# Non-Repeating value Summation in Matrix
res = sum(list(set(chain(*test_matrix))))

# printing result
print ("Unique values summation in matrix are : " + str(res))

# Python3 code to demonstrate
# checking unique values in matrix
# chain() + set()
from itertools import chain

# initializing matrix
test_matrix = [[1, 3, 1], [4, 5, 3], [1, 2, 4]]

# printing the original matrix
print ("The original matrix is : " + str(test_matrix))

# using chain() + set()
# for checking unique values in matrix
res = list(set(chain(*test_matrix)))

# printing result
print ("Unique values in matrix are : " + str(res))

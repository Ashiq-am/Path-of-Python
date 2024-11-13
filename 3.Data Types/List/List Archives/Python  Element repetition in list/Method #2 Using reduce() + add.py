# Python3 code to demonstrate
# to perform element duplication
# using reduce() + add
from operator import add

# initializing list
test_list = [4, 5, 6, 3, 9]

# printing original list
print ("The original list is : " + str(test_list))

# using reduce() + add
# to perform element duplication
res = list(reduce(add, [(i, i) for i in test_list]))

# printing result
print ("The list after element duplication " + str(res))

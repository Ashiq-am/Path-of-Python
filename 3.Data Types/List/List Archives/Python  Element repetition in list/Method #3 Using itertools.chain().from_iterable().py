# Python3 code to demonstrate
# to perform element duplication
# using itertools.chain.from_iterable()
import itertools

# initializing list
test_list = [4, 5, 6, 3, 9]

# printing original list
print ("The original list is : " + str(test_list))

# using itertools.chain.from_iterable()
# to perform element duplication
res = list(itertools.chain.from_iterable([i, i] for i in test_list))

# printing result
print ("The list after element duplication " + str(res))

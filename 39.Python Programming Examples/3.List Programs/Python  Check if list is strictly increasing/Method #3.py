# Python3 code to demonstrate
# to check for strictly increasing list
# using itertools.starmap() + zip() + all()
import operator
import itertools

# initializing list
test_list = [1, 4, 5, 7, 8, 10]

# printing original lists
print ("Original list : " + str(test_list))

# using itertools.starmap() + zip() + all()
# to check for strictly increasing list
res = all(itertools.starmap(operator.le,
		zip(test_list, test_list[1:])))

# printing result
print ("Is list strictly increasing ? : " + str(res))

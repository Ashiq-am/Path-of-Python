# Python3 code to demonstrate
# increasing alternate element pattern
# using itertools.chain.from_iterable() + zip()
import itertools

# initializing list
test_list = [1, 2, 3, 4, 5]

# printing original list
print("The original list : " + str(test_list))

# using itertools.chain.from_iterable() + zip()
# increasing alternate element pattern
res = list(itertools.chain.from_iterable(
			zip(test_list, ("*" * (i + 1)
			for i in range(len(test_list))))))

# print result
print("The increasing element pattern list : " + str(res))

# Python3 code to demonstrate working of
# Check if all elements in list follow a condition
# Using itertools.takewhile()
import itertools

# initializing list
test_list = [4, 5, 8, 9, 10]

# printing list
print("The original list : " + str(test_list))

# Check if all elements in list follow a condition
# Using itertools.takewhile()
count = 0
for ele in itertools.takewhile(lambda x: x > 3, test_list):
	count = count + 1
res = count == len(test_list)

# Printing result
print("Are all elements greater than 3 ? : " + str(res))

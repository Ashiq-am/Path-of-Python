# Python code to demonstrate
# Smallest number from list
# using sorted() + lambda
import functools

# initializing list
test_list = [23, 65, 98, 3, 4]

# printing original list
print ("The original list is : " + str(test_list))

# lambda for custom operation
custom = lambda i, j: -1 if str(j) + str(i) > str(i) + str(j) else 1

# using sorted() + custom function
# Smallest number from list
res = sorted(test_list, key = functools.cmp_to_key(custom))


# printing result
print ("The smallest possible number : " + "".join(map(str, res)))

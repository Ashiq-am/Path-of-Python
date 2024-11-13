# Python3 code to demonstrate
# Uneven Sized Matrix Column Minimum
# using list comprehension + min() + zip_longest()
import itertools

# initializing list of lists
test_list = [[1, 5, 3], [4], [9, 8]]

# printing original list
print ("The original list is : " + str(test_list))

# using list comprehension + min() + zip_longest()
# Uneven Sized Matrix Column Minimum
res = [min(i) for i in itertools.zip_longest(*test_list, fillvalue = 1000000)]

# printing result
print ("The minimum of columns is : " + str(res))

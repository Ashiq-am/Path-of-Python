# Python3 code to demonstrate
# Column summation in uneven sized lists
# using list comprehension + sum() + zip_longest()
import itertools

# initializing list of lists
test_list = [[1, 5, 3], [4], [9, 8]]

# printing original list
print ("The original list is : " + str(test_list))

# using list comprehension + sum() + zip_longest()
# Column summation in uneven sized lists
res = [sum(i) for i in itertools.zip_longest(*test_list, fillvalue = 0)]

# printing result
print ("The summation of columns is : " + str(res))

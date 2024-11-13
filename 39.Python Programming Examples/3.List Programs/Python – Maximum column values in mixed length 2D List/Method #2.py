# Python3 code to demonstrate
# Maximum column values mixed length 2D List
# using list comprehension + max() + zip_longest()
import itertools

# initializing list of lists
test_list = [[1, 5, 3], [4], [9, 8]]

# printing original list
print ("The original list is : " + str(test_list))

# using list comprehension + max() + zip_longest()
# Maximum column values mixed length 2D List
res = [max(i) for i in itertools.zip_longest(*test_list, fillvalue = 0)]

# printing result
print ("The maximization of columns is : " + str(res))

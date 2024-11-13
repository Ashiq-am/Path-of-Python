# Python code to demonstrate
# addition of two list
# zip() + sum()
from operator import add

# initializing lists
test_list1 = [1, 3, 4, 6, 8]
test_list2 = [4, 5, 6, 2, 10]

# printing original lists
print ("Original list 1 : " + str(test_list1))
print ("Original list 2 : " + str(test_list2))

# using zip() + sum() to
# add two list
res_list = [sum(i) for i in zip(test_list1, test_list2)]

# printing resultant list
print ("Resultant list is : " + str(res_list))

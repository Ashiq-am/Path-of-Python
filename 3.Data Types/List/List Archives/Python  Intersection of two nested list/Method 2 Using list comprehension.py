# Python 3 code to demonstrate
# find intersection of nested list
# using list comprehension

# initializing lists
test_list1 = [ [1, 2], [3, 4], [5, 6] ]
test_list2 = [ [3, 4], [5, 7], [1, 2] ]

# printing both lists
print ("The original list 1 : " + str(test_list1))
print ("The original list 2 : " + str(test_list2))

# using list comprehension
# to get list intersection
res_list = [i for i in test_list1 if i in test_list2]

# printing the intersection
print ("The intersection of two lists is : " + str(res_list))

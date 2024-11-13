# Python3 code to demonstrate
# Integer count in Mixed List
# using list comprehension + len() + isinstance()

# initializing list
test_list = [3, 'computer', 5, 'geeks', 6, 7]

# printing original list
print ("The original list is : " + str(test_list))

# using list comprehension + len() + isinstance()
# Integer count in Mixed List
res = len(list(i for i in test_list if isinstance(i, int)))

# printing result
print ("The length of integers in list is : " + str(res))

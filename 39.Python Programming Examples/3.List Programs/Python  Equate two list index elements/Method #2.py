# Python3 code to demonstrate
# Equate two list index elements
# using join() + zip()

# initializing lists
test_list1 = ['GeeksforGeeks', 'is', 'best']
test_list2 = ['1', '2', '3']

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# using join() + zip() to
# Equate two list index elements
res = ', '.join('% s = % s' % i for i in zip(test_list1, test_list2))

# printing result
print ("The paired elements string is : " + res)

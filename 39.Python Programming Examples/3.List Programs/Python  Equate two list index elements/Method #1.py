# Python3 code to demonstrate
# Equate two list index elements
# using formatting + tuple()

# initializing lists
test_list1 = ['GeeksforGeeks', 'is', 'best']
test_list2 = ['1', '2', '3']

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# using formatting + tuple() to
# Equate two list index elements
temp = len(test_list1) * '% s = %% s, '
res = temp % tuple(test_list1) % tuple(test_list2)

# printing result
print ("The paired elements string is : " + res)

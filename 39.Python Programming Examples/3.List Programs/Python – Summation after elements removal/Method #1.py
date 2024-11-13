# Python 3 code to demonstrate
# Summation after elements removal
# using list comprehension + sum()

# initializing list
test_list = [1, 3, 4, 6, 7, 6]

# initializing remove list
remove_list = [3, 6]

# printing original list
print ("The original list is : " + str(test_list))

# printing remove list
print ("The remove list is : " + str(remove_list))

# using list comprehension + sum() to perform task
res = sum([i for i in test_list if i not in remove_list])

# printing result
print ("The list after performing removal summation is : " + str(res))

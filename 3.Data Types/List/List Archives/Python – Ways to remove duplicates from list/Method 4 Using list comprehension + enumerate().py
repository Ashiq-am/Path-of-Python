# Python 3 code to demonstrate
# removing duplicated from list
# using list comprehension + enumerate()

# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : " + str(test_list))

# using list comprehension + enumerate()
# to remove duplicated
# from list
res = [i for n, i in enumerate(test_list) if i not in test_list[:n]]

# printing list after removal
print ("The list after removing duplicates : " + str(res))

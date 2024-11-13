# Python3 code to demonstrate
# Truth values deletion in List
# using list comprehension

# initializing list
test_list = [1, None, 4, None, False, 5, 8, False]

# printing original list
print ("The original list is : " + str(test_list))

# using list comprehension
# Truth values deletion in List
res = [i for i in test_list if not i]

# printing result
print ("List after removal of Truth values : " + str(res))

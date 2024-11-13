# Python3 code to demonstrate
# Odd elements removal in List
# using list comprehension

# initializing list
test_list = [1, 9, 4, 7, 6, 5, 8, 3]

# printing original list
print ("The original list is : " + str(test_list))

# using list comprehension
# Odd elements removal in List
res = [i for i in test_list if not (i % 2 != 0)]

# printing result
print ("List after removal of odd values : " + str(res))

# Python3 code to demonstrate
# Diagonal element addition among lists
# using zip() + list comprehension

# Initializing lists
test_list1 = [1, 6, 8, 5, 3]
test_list2 = [8, 10, 3, 4, 5]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Diagonal element addition among lists
# using zip() + list comprehension
res = [i + j for i, j in zip(test_list1, test_list2[1:])]

# printing result
print ("List after diagonal addition : " + str(res))

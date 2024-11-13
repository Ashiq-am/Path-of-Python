# Python3 code to demonstrate
# K Summation from Two lists
# using list comprehension

# Initializing lists
test_list1 = [3, 2, 5]
test_list2 = [4, 3, 6, 8, 7]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Initializing K
K = 9

# K Summation from Two lists
# using list comprehension
res = [(a, b) for a in test_list1 for b in test_list2 if a + b == K]

# printing result
print ("Summation pairs among lists : " + str(res))

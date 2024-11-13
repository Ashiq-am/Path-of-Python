# Python3 code to demonstrate working of
# Custom Lowerbound a List
# Using list comprehension

# initializing list
test_list = [5, 7, 8, 2, 3, 5, 1]

# printing original list
print("The original list is : " + str(test_list))

# initializing Lowerbound
K = 4

# checking for elements and assigning Lowerbounds
res = [ele if ele >= K else K for ele in test_list]

# printing result
print("List with Lowerbounds : " + str(res))

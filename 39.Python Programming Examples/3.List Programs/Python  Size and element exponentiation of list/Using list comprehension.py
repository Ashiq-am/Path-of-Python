# Python3 code to demonstrate working of
# Size and element exponentiation of list
# Using list comprehension

# initializing list
test_list = [4, 5, 6]

# printing original list
print("The original list is : " + str(test_list))

# Extension factor
N = 4

# Exponentiation factor
M = 3

# Size and element exponentiation of list
# Using list comprehension
temp = [1 * M**i for i in range(N)]
res = list([ele ** tele for tele in temp for ele in test_list])

# printing result
print("List after extension and exponentiation : " + str(res))

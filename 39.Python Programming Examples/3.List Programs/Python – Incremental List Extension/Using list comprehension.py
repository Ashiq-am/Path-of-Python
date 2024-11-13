# Python3 code to demonstrate working of
# Incremental List Extension
# Using list comprehension

# initializing list
test_list = [7, 8, 9]

# printing original list
print("The original list is : " + str(test_list))

# Extension factor
N = 4

# Addition factor
M = 3

# Incremental List Extension
# Using list comprehension
temp = [1 * M**i for i in range(N)]
temp[0] = 0
res = list([ele + tele for tele in temp for ele in test_list])

# printing result
print("List after extension and addition : " + str(res))

# Python3 code to demonstrate working of
# Rear column in Multisized Matrix
# Using list comprehension

# initializing list
test_list = [[3, 4, 5], [7], [8, 4, 6, 1], [10, 3]]

# printing original list
print("The original list is : " + str(test_list))

# one-liner to solve this problem
res = [sub[-1] for sub in test_list]

# printing results
print("Filtered column : " + str(res))

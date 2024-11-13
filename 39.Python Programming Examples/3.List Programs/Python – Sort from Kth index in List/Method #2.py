# Python3 code to demonstrate working of
# Perform sort from Kth index
# Using Using double List slicing

# initializing list
test_list = [8, 4, 7, 3, 2, 14, 6]

# printing original list
print("The original list : " + str(test_list))

# initialzing K
K = 3

# Using loop + list slicing
res = []

# Using loop to extract elements till K
# Concatenating unsort and sorted part as one liner
res = test_list[:K] + sorted(test_list[K:])

# printing result
print("Partially sorted list : " + str(res))

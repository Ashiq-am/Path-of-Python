# Python3 code to demonstrate
# Closest Sum Pair in List
# using dictionary comprehension + max()

# Initializing list
test_list = [7, 8, 10, 3, 18, 1]

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 12

# Closest Sum Pair in List
# using dictionary comprehension + max()
test_list.sort()
res = { i + j :(i, j) for i in test_list for j in test_list if i != j and i + j < K}
res = max(res)

# printing result
print ("The closest sum pair is : " + str(res))

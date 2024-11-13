# Python3 code to demonstrate working of
# Redistribute Trimmed Values
# Using slice() + sum()

# initializing list
test_list = [4, 5, 2, 8, 9, 3, 1, 2, 4]

# printing original lists
print("The original list is : " + str(test_list))

# initializing K
K = 2

# getting full list sum
full_sum = sum(test_list)

# trimming list
trimd_list = test_list[K:len(test_list) - K]

# getting trimmed list sum
trim_sum = sum(trimd_list)

# getting value to add to each element
add_val = (full_sum - trim_sum) / len(trimd_list)

# adding values
res = [ele + add_val for ele in trimd_list]

# printing result
print("Redistributed list : " + str(res))

# Python3 code to demonstrate working of
# Extend consecutive tuples
# Using loop

# initializing list
test_list = [(3, 5, 6, 7), (3, 2, 4, 3), (9, 4), (2, 3, 2), (3,), (3, 6)]

# printing original list
print("The original list is : " + str(test_list))

res = []
for idx in range(len(test_list) - 1):
    # joining tuples
    res.append(test_list[idx] + test_list[idx + 1])

# printing results
print("Joined tuples : " + str(res))

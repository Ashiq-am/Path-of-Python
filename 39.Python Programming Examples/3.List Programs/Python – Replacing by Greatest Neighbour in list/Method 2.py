# Python3 code to demonstrate working of
# Replacing by Greatest Neighbour
# Using max() + loop

# initializing list
test_list = [5, 4, 2, 5, 8, 2, 1, 9]

# printing original list
print("The original list is : " + str(test_list))

for idx in range(1, len(test_list) - 1):
    # using max() to get maximum of Neighbours
    test_list[idx] = max(test_list[idx - 1], test_list[idx + 1])

# printing result
print("The elements after replacing : " + str(test_list))

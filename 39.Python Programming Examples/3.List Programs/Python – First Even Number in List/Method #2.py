# Python3 code to demonstrate
# First Even Number in List
# using binary search

# Initializing list
test_list = [3, 7, 8, 9, 10, 15]

# printing original list
print("The original list is : " + str(test_list))

# First Even Number in List
# using binary search
res = len(test_list)
low = 0
high = len(test_list) - 1
while low <= high:
    mid = (low + high) // 2
    if test_list[mid] % 2:
        low = mid + 1
    else:
        res = test_list[mid]
        high = mid - 1

# printing result
print("The first even element in list is : " + str(res))

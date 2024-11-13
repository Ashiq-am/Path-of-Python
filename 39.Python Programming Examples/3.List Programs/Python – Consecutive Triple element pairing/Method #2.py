# Python3 code to demonstrate
# Consecutive Triple element pairing
# using zip() + map()

# initializing list
test_list = [5, 4, 1, 3, 2]

# printing original list
print("The original list : " + str(test_list))

# using zip() + map()
# Consecutive Triple element pairing
res = list(map(list, zip(test_list, test_list[1:], test_list[2:])))

# print result
print("The consecutive element triple paired list is : " + str(res))

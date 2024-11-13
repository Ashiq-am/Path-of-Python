# Python3 code to demonstrate
# Consecutive Triple element pairing
# using list comprehension

# initializing list
test_list = [5, 4, 1, 3, 2]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension
# Consecutive Triple element pairing
res = [[test_list[i], test_list[i + 1], test_list[i + 2]] for i in range(len(test_list) - 2)]

# print result
print("The consecutive element triple paired list is : " + str(res))

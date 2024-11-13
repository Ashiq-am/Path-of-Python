# Python3 code to demonstrate
# Consecutive Subsets Minimum
# using list comprehension + min()

# initializing list
test_list = [4, 7, 8, 10, 12, 15, 13, 17, 14]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + min()
# Consecutive Subsets Minimum
res = [ min(test_list[x : x + 3]) for x in range(0, len(test_list), 3)]

# printing result
print("The grouped minimum list is : " + str(res))

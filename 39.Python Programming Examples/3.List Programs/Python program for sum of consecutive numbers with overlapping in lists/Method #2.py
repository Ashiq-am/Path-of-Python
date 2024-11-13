# Python3 code to demonstrate working of
# Consecutive overlapping Summation
# Using sum() + list comprehension + zip()

# initializing list
test_list = [4, 7, 3, 2, 9, 2, 1]

# printing original list
print("The original list is : " + str(test_list))

# using sum() to compute elements sum
# last element is joined with first for pairing
res = [sum(sub) for sub in zip(test_list, test_list[1:] + [test_list[0]])]

# printing result
print("The Consecutive overlapping Summation : " + str(res))

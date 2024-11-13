# initializing list
test_list = [4, 7, 3, 2, 9, 2, 1]

# printing original list
print("The original list is : " + str(test_list))

# using zip() to get pairing.
# last element is joined with first for pairing
res = [a + b for a, b in zip(test_list, test_list[1:] + [test_list[0]])]

# printing result
print("The Consecutive overlapping Summation : " + str(res))

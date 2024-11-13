# Python3 code to demonstrate
# Mean of consecutive Sublist
# using list comprehension + sum()

# initializing list
test_list = [4, 7, 8, 10, 12, 15, 13, 17, 14]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + sum()
# Mean of consecutive Sublist
res = [ sum(test_list[x : x + 3]) / 3 for x in range(0, len(test_list), 3)]

# printing result
print("The grouped average list is : " + str(res))

# Python3 code to demonstrate working of
# Sort by Units Digit in List
# Using sorted() + lambda + str()

# initializing lists
test_list = [76, 434, 23, 22342]

# printing original lists
print("The original list is : " + str(test_list))

# inplace sort by unit digits
res = sorted(test_list, key=lambda sub: str(sub)[-1])

# printing result
print("The unit sorted list : " + str(res))

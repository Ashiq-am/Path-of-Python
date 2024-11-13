# Python3 code to demonstrate working of
# Filter Sorted Rows
# Using filter() + lambda + sorted() + reverse

# initializing list
test_list = [[3, 6, 8, 10], [1, 8, 2, 4, 3], [8, 5, 3, 2], [1, 4, 5, 3]]

# printing original list
print("The original list is : " + str(test_list))

# filtering using sorted() and reverse as key
res = list(filter(lambda sub: sub == list(sorted(sub)) or sub ==
				list(sorted(sub, reverse=True)), test_list))

# printing result
print("Extracted rows : " + str(res))

# Python3 code to demonstrate working of
# Test if Rows have Similar frequency
# Using list comprehension + sorted() + all()

# initializing list
test_list = [[6, 4, 2, 7, 3], [7, 3, 6, 4, 2], [2, 4, 7, 3, 6]]

# printing original list
print("The original list is : " + str(test_list))

# checking if all rows are similar
# ordering each row to test
res = all(list(sorted(row)) == list(sorted(test_list[0])) for row in test_list)

# printing result
print("Are all rows similar : " + str(res))

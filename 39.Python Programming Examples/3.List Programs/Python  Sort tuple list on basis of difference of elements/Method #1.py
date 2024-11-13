# Python3 code to demonstrate working of
# Sort tuple list on basis of difference of elements
# using sorted() + lambda

# initialize list
test_list = [(1, 4), (6, 5), (8, 10)]

# printing original list
print("The original list : " + str(test_list))

# Sort tuple list on basis of difference of elements
# using sorted() + lambda
res = sorted(test_list, key = lambda sub: abs(sub[1] - sub[0]))

# printing result
print("List after sorting by difference : " + str(res))

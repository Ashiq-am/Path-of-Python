# Python3 code to demonstrate working of
# Sort Strings in String list
# using map() + sorted() + join() + lambda

# initialize list
test_list = ['gfg', 'is', 'good']

# printing original list
print("The original list : " + str(test_list))

# Sort Strings in String list
# using map() + sorted() + join() + lambda
res = list(map(lambda ele: "".join(sorted(ele)), test_list))

# printing result
print("List after string sorting : " + str(res))

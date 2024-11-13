# Python3 code to demonstrate working of
# Alternate Sort String list
# using join() + enumerate() + generator expression + sorted()

# initialize list
test_list = ['cdab', 'gfeh', 'kjil']

# printing original list
print("The original list : " + str(test_list))

# Alternate Sort String list
# using join() + enumerate() + generator expression + sorted()
res = ["".join(sorted(j, reverse = i % 2)) for i, j in enumerate(test_list)]

# printing result
print("The String list after alternate sorting : " + str(res))

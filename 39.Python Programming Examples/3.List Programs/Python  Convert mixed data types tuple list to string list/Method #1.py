# Python3 code to demonstrate working of
# Convert tuple mixed list to string list
# using list comprehension + tuple() + str() + generator expression

# initialize list
test_list = [('gfg', 1, True), ('is', False), ('best', 2)]

# printing original list
print("The original list : " + str(test_list))

# Convert tuple mixed list to string list
# using list comprehension + tuple() + str() + generator expression
res = [tuple(str(ele) for ele in sub) for sub in test_list]

# printing result
print("The tuple list after conversion : " + str(res))

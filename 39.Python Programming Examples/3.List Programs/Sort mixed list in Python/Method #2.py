# Python3 code to demonstrate working of
# Sort Mixed List
# using sorted() + key + lambda + isdigit()

# initialize list
test_list = ['4', 'gfg', '2', 'best', 'is', '3']

# printing original list
print("The original list : " + str(test_list))

# Sort Mixed List
# using sorted() + key + lambda + isdigit()
res = sorted(test_list, key = lambda ele: (0, int(ele))
						if ele.isdigit() else (1, ele))

# printing result
print("List after mixed sorting : " + str(res))

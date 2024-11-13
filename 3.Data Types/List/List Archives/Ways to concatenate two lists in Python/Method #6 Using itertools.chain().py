# Python3 code to demonstrate list
# concatenation using itertools.chain()
import itertools

# Initializing lists
test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]

# using itertools.chain() to concat
res_list = list(itertools.chain(test_list1, test_list2))

# Printing concatenated list
print ("Concatenated list using itertools.chain() : "
									+ str(res_list))

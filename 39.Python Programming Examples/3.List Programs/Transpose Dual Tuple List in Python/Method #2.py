# Python3 code to demonstrate working of
# Transpose Tuple List
# Using zip() + tuple()

# hlper_fnc function
def hlper_fnc(test_list):
	return tuple(zip(*test_list))

# initializing list
test_list = [(5, 1), (3, 4), (9, 7), (10, 6)]

# printing original list
print("The original list is : " + str(test_list))

# Transpose Tuple List
# Using zip() + tuple()
sub1, sub2 = hlper_fnc(test_list)
res = (list(sub1), list(sub2))

# printing result
print("The transposed tuple list : " + str(res))

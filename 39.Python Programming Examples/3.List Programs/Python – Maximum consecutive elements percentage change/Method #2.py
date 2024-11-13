# Python3 code to demonstrate working of
# Maximum consecutive elements percentage change
# Using zip() + loop

# helpr_fnc
def get_max_diff(test_list, curr_max = None):
	pot_max = (abs(test_list[1] - test_list[0]) / test_list[0]) * 100
	if curr_max :
		pot_max = max(curr_max, pot_max)
	if len(test_list) == 2:
		return pot_max
	return get_max_diff(test_list[1:], pot_max)

# initializing list
test_list = [4, 6, 7, 4, 2, 6, 2, 8]

# printing original list
print("The original list is : " + str(test_list))

# Maximum consecutive elements percentage change
# Using zip() + loop
res = get_max_diff(test_list)

# printing result
print("The maximum percentage change : " + str(res))

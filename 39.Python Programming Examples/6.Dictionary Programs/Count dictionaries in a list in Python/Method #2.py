# Python3 code to demonstrate working of
# Dictionary Count in List
# Using recursion + isinstance()

# helper_func
def hlper_fnc(test_list):
	count = 0
	if isinstance(test_list, str):
		return 0
	if isinstance(test_list, dict):
		return hlper_fnc(test_list.values()) + hlper_fnc(test_list.keys()) + 1
	try:
		for idx in test_list:
			count = count + hlper_fnc(idx)
	except TypeError:
		return 0
	return count

# initializing list
test_list = [10, {'gfg': 1}, {'code': 3, 'ide': 2}, 20]

# printing original list
print("The original list is : " + str(test_list))

# Dictionary Count in List
# Using recursion + isinstance()
res = hlper_fnc(test_list)

# printing result
print("The Dictionary count : " + str(res))

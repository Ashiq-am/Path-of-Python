# getting max value
def get_max(dicts):
	return max(list(dicts.values()))


# initializing list
test_list = [{1: 5, 6: 7, 9: 1}, {2: 6, 9: 10, 1: 4}, {6: 5, 9: 3, 1: 6}]

# printing original list
print("The original list is : " + str(test_list))

# sorting dictionary list by maximum value
test_list.sort(key=get_max)

# printing result
print("Sorted List : " + str(test_list))

# Python3 code to demonstrate working of
# Sort Matrix by total characters
# Using sort() + len() + sum()


def total_chars(row):

	# getting total characters
	return sum([len(sub) for sub in row])


# initializing list
test_list = [["Gfg", "is", "Best"], ["Geeksforgeeks", "Best"],
			["GFg", "4", "good"], ["ILvGFG"]]

# printing original list
print("The original list is : " + str(test_list))

# calling utility fnc
test_list.sort(key=total_chars)

# printing result
print("Sorted results : " + str(test_list))

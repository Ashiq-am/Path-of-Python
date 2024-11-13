# Python3 code to demonstrate working of
# Reversed Pairs in Strings List
# Using reversed() + loop

# initializing Matrix
test_list = ["geeks", "best", "tseb", "for", "skeeg"]

# printing original list
print("The original list is : " + str(test_list))

res = 0
for idx in range(0, len(test_list)):

	# nested loop to check with each element with possible reverse counterpart
	for idxn in range(idx, len(test_list)):
		if test_list[idxn] == str(''.join(list(reversed(test_list[idx])))):
			res += 1

# printing result
print("Reversed Pairs : " + str(res))

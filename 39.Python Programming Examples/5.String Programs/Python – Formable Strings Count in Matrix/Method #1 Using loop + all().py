# Python3 code to demonstrate working of
# Formable Strings Count in Matrix
# Using loop

# initializing list
test_list = [["gfg", "best"], ["all", "love", "gfg"],
			["gfg", "is", "good"], ["geeksforgeeks"]]

# printing original list
print("The original list is : " + str(test_list))

# initializing target list
tar_list = ["g", "f", "s", "b", "o", "d", "e", "t"]

res = 0
for sub in test_list:
	for ele in sub:

		# checking for all elements present using all()
		if all(el in tar_list for el in ele):
			res += 1

# printing result
print("The computed count : " + str(res))

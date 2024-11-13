# Python3 code to demonstrate working of
# Formable Strings Count in Matrix
# Using list comprehension + all() + sum()

# initializing list
test_list = [["gfg", "best"], ["all", "love", "gfg"],
			["gfg", "is", "good"], ["geeksforgeeks"]]

# printing original list
print("The original list is : " + str(test_list))

# initializing target list
tar_list = ["g", "f", "s", "b", "o", "d", "e", "t"]

# computing summation using sum()
# list comprehension used to provide one liner solution
res = sum([sum([1 for ele in sub if all(el in tar_list for el in ele)])
		for sub in test_list])

# printing result
print("The computed count : " + str(res))

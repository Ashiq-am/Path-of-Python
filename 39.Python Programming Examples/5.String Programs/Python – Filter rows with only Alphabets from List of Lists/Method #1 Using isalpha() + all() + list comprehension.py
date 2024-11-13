# Python3 code to demonstrate working of
# Filter rows with only Alphabets
# Using isalpha() + all() + list comprehension

# initializing list
test_list = [["gfg", "is", "best"], ["Geeks4Geeks", "good"],
			["Gfg is good"], ["love", "gfg"]]

# printing original lists
print("The original list is : " + str(test_list))

# all() checks for all strings to contain alphabets
res = [sub for sub in test_list if all(ele.isalpha() for ele in sub)]

# printing result
print("Filtered Rows : " + str(res))

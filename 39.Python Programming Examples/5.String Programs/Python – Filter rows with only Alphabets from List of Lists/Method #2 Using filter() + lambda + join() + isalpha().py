# Python3 code to demonstrate working of
# Filter rows with only Alphabets
# Using filter() + lambda + join() + isalpha()

# initializing list
test_list = [["gfg", "is", "best"], ["Geeks4Geeks", "good"],
			["Gfg is good"], ["love", "gfg"]]

# printing original lists
print("The original list is : " + str(test_list))

# join() used to concatenate strings
res = list(filter(lambda sub: ''.join(
	[ele for ele in sub]).isalpha(), test_list))

# printing result
print("Filtered Rows : " + str(res))

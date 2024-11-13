# initializing Matrix
test_list = ["gfg", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

res = ""
max_len = 0
for ele in test_list:

	# getting maximum length and element
	# iteratively
	vow_len = len([el for el in ele if el in ['a', 'e', 'o', 'u', 'i']])
	if vow_len > max_len:
		max_len = vow_len
		res = ele

# printing result
print("Maximum vowels word : " + str(res))

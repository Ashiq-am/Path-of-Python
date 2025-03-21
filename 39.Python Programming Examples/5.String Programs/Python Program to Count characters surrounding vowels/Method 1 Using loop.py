# initializing string
test_str = 'geeksforgeeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

res = 0
vow_list = ['a', 'e', 'i', 'o', 'u']
for idx in range(1, len(test_str) - 1):

	# checking for preceding and succeeding element to be vowel
	if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
		res += 1

# solving for 1st and last element
if test_str[0] not in vow_list and test_str[1] in vow_list:
	res += 1

if test_str[-1] not in vow_list and test_str[-2] in vow_list:
	res += 1

# printing result
print("Characters around vowels count : " + str(res))

# initializing list
test_list = ["google", "is", "good", "goggled", "god"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 'g'

res = []
for sub in test_list:

	# joining only K characters
	res.append(''.join([ele for ele in sub if ele == K]))

# printing result
print("Modified List : " + str(res))

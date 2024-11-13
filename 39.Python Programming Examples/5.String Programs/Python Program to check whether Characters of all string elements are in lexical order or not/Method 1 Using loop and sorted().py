# initializing list
test_list = ["dent", "flop", "most", "cent"]

# printing original list
print("The original list is : " + str(test_list))

res = True
for ele in test_list:

	# check for ordered string
	if ele != ''.join(sorted(ele)):
		res = False
		break

# printing result
print("Are all strings ordered ? : " + str(res))

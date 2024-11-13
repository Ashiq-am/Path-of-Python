# Python3 code to demonstrate working of
# Selective consecutive Suffix Join
# Using loop + endswith() + join()

# initializing list
test_list = ["Geeks-", "for-", "Geeks", "is",
			"best-", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing suffix
suff = '-'

res = []
temp = []
for ele in test_list:
	temp.append(ele)

	# conditionally test values
	if not ele.endswith(suff):
		res.append(''.join(temp))
		temp = []
if temp:
	res.append(''.join(temp))

# printing result
print("The joined result : " + str(res))

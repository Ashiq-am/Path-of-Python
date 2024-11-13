# initializing string
test_str = "geeksforgeeks is best for all geeks"

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = '$'

# initializing N
N = 5

res = ''
for idx, ele in enumerate(test_str):

	# add K if idx is multiple of N
	if idx % N == 0 and idx != 0:
		res = res + K
	else:
		res = res + ele

# printing result
print("String after replacement : " + str(res))

# initializing string
test_str = "geeksforgeeks is best for all geeks"

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = '$'

# initializing N
N = 5

res = ''.join(ele if idx % N or idx == 0 else K for idx,
			ele in enumerate(test_str))

# printing result
print("String after replacement : " + str(res))

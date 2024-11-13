# Python3 code to demonstrate working of
# Extract characters except of K string
# Using loop

# initializing strings
test_str1 = "geeksforgeeks is best"
test_str2 = "fes"

# printing original strings
print("The original string 1 is : " + test_str1)
print("The original string 2 is : " + test_str2)

# Extract characters except of K string
# Using loop
res = []
for ele in test_str1:
	if ele not in test_str2:
		res.append(ele)
res = ''.join(res)

# printing result
print("String after removal of substring elements : " + str(res))

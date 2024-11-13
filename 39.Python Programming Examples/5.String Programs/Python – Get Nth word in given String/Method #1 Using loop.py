# Python3 code to demonstrate working of
# Get Nth word in String
# using loop

# initializing string
test_str = "GFG is for Geeks"

# printing original string
print("The original string is : " + test_str)

# initializing N
N = 3

# Get Nth word in String
# using loop
count = 0
res = ""
for ele in test_str:
	if ele == ' ':
		count = count + 1
		if count == N:
			break
		res = ""
	else :
		res = res + ele

# printing result
print("The Nth word in String : " + res)

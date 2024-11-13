# Python3 code to demonstrate working of
# Iterative Pair Pattern
# Using loop

# initializing 1st element
frst_ele = 'G'

# initializing 2nd element
secnd_ele = '*'

# initializing N
N = 4

# Iterative Pair Pattern
# Using loop
res = frst_ele + secnd_ele
for idx in range(1, N):
	res += frst_ele + secnd_ele * (idx + 1)

# printing result
print("The constructed pattern is : " + str(res))

# Python 3 code to demonstrate
# Nth smallest Greater than K
# using naive method + sort()

# Initializing list
test_list = [1, 4, 7, 5, 10]

# Initializing k
k = 6

# Initializing N
N = 2

# Printing original list
print ("The original list is : " + str(test_list))

# Using naive method + sort()
# Nth smallest Greater than K
res = []
for i in test_list :
	if i > k :
		res.append(i)
res.sort()

# Printing result
print ("The Nth minimum value greater than 6 is : " + str(res[N - 1]))

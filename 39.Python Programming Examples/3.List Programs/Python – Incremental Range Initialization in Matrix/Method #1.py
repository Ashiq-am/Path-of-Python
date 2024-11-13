# Python3 code to demonstrate
# Incremental Range Initialization in Matrix
# using loop

# Initializing row
r = 4

# Initializing col
c = 3

# Initializing range
rang = 5

# Incremental Range Initialization in Matrix
# using loop
res = []
temp = []
temp2 = 0
for idx in range(r):
	for idx in range(c):
		temp.append(temp2)
		temp2 = temp2 + rang
	res.append(temp)
	temp = []

# printing result
print ("Matrix after Initialization : " + str(res))

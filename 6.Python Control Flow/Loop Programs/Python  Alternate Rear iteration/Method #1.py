# Python3 code to demonstrate
# Alternate Rear iteration
# using reversed()

# Initializing number from which
# iteration begins
N = 6

# using reversed() to perform the Alternate Rear iteration
print ("The reversed numbers are : ", end = "")
for num in reversed(range(0, N + 1, 2)) :
	print (num, end = " ")

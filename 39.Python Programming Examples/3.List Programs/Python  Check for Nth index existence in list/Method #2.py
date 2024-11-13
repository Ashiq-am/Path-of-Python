# Python3 code to demonstrate working of
# Check for Nth index existence in list
# Using try-except block + IndexError exception

# initializing list
test_list = [4, 5, 6, 7, 10]

# printing original list
print("The original list is : " + str(test_list))

# initializing N
N = 6

# Check for Nth index existence in list
# Using try-except block + IndexError exception
try:
	val = test_list[N]
	res = True
except IndexError:
	res = False

# printing result
print("Is Nth index available? : " + str(res))

# defining truncate function
# second argument defaults to 0
# so that if no argument is passed
# it returns the integer part of number

def truncate(n, decimals = 0):
	multiplier = 10 ** decimals
	return int(n * multiplier) / multiplier

print(truncate(16.5))
print(truncate(-3.853, 1))
print(truncate(3.815, 2))

# we can truncate digits towards the left of the decimal point
# by passing a negative number.
print(truncate(346.8, -1))
print(truncate(-2947.48, -3))

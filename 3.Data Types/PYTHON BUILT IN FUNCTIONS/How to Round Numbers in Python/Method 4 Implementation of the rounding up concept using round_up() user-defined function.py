# import math library
import math

# define a function for
# round_up
def round_up(n, decimals = 0):
	multiplier = 10 ** decimals
	return math.ceil(n * multiplier) / multiplier

# passing positive values
print(round_up(2.1))
print(round_up(2.23, 1))
print(round_up(2.543, 2))

# passing negative values
print(round_up(22.45, -1))
print(round_up(2352, -2))

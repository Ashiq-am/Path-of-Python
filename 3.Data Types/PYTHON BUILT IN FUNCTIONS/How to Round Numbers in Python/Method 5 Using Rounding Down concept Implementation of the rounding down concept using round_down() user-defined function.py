import math

# defining a function for
# round down.
def round_down(n, decimals=0):
	multiplier = 10 ** decimals
	return math.floor(n * multiplier) / multiplier

# passing different values to function
print(round_down(2.5))
print(round_down(2.48, 1))
print(round_down(-0.5))

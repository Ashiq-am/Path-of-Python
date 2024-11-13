import math

# defining round_half_up

def round_half_up(n, decimals=0):
	multiplier = 10 ** decimals
	return math.floor(n * multiplier + 0.5) / multiplier

# passing different values to the function

print(round_half_up(1.28, 1))
print(round_half_up(-1.5))
print(round_half_up(-1.225, 2))

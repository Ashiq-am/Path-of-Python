# Demonstrate ValueError while
# doing forced type-conversions

# When explicitly converted floating-point
# values to decimal with base-10 by 'd'
# type conversion we encounter Value-Error.
print("The temperature today is {0:d} degrees outside !"
										.format(35.567))

# Instead write this to avoid value-errors
''' print("The temperature today is {0:.0f} degrees outside !" 
											.format(35.567))'''

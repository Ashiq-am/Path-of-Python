import math


x = math.nan
print(f"x contains {x}")

# checks if variable is equal to NaN
if(math.isnan(x)):
	print("x == nan")
else:
	print("x != nan")

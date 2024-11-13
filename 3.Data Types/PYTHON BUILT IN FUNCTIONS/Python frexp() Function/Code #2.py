# Python3 code demonstrate frexp() function

# importing math library
import math

# creating a list
lst = [15, 13.76, 17.5, 21]

# creating a tuple
tpl = (-15.85, -41.24, -11.2, 54)

# calculating mantissa and exponent
# of 1st, 3rd elements in list
print(math.frexp(lst[0]))
print(math.frexp(lst[2]))

# calculating mantissa and exponent
# of 2nd, 3rd and 4th elements in tuple
print(math.frexp(tpl[1]))
print(math.frexp(tpl[2]))
print(math.frexp(tpl[3]))

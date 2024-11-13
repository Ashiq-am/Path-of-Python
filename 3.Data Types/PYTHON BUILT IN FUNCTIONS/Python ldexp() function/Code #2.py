# Python3 code demonstrate ldexp() function

# importing math library
import math

# Tuple Declaration
tpl = (9, -5, 3.5, -6.8)

# List Declaration
lst = [13, 4, 8.4, -6.7]

# ldexp() Function on +ve nd -ve Numbers
print(math.ldexp(tpl[0], 3))
print(math.ldexp(tpl[3], 2))

# ldexp() Function on fractional Number
print(math.ldexp(lst[1], 2))
print('%.2f' %math.ldexp(lst[2], 3))

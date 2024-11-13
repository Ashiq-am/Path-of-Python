# Python3 program to demonstrate
# errors in fmod() function

import math

# will give ValueError
print(math.fmod(0, 0))
print(math.fmod(2, 0))

# it will give TypeError
print(math.fmod('2', 3))

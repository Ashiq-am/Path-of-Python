# Python program explaining
# numpy.angle() function
# when we want answer in degrees

import numpy as geek

in_list = [2.0, 1.0j, 1 + 1j]

print("Input list : ", in_list)

out_angle = geek.angle(in_list, deg=True)
print("output angle in degrees : ", out_angle)

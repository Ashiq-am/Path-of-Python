# Python program explaining
# numpy.angle() function
# when we want answer in radian

import numpy as geek

in_list = [2.0, 1.0j, 1 + 1j]

print("Input list : ", in_list)

out_angle = geek.angle(in_list)
print("output angle in radians : ", out_angle)

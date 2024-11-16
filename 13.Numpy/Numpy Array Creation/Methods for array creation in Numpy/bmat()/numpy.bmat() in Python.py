# Python Program illustrating
# numpy.bmat

import numpy as geek

A = geek.mat('4 1; 22 1')
B = geek.mat('5 2; 5 2')
C = geek.mat('8 4; 6 6')

# array like igeekut
a = geek.bmat([[A, B], [C, A]])
print("Via bmat array like input : \n", a, "\n\n")

# string like igeekut
s = geek.bmat('A, B; A, A')
print("Via bmat string like input : \n", s)

# Python program explaining
# numpy.typename() function

# importing numpy as geek
import numpy as geek

typechars = ['?', 'O', 'b', 'd', 'g', 'f', 'i', 'h', 'l', 'q']

for typechar in typechars:
    print(typechar, ' : ', geek.typename(typechar))

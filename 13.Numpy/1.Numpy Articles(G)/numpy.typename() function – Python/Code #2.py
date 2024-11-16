# Python program explaining
# numpy.typename() function

# importing numpy as geek
import numpy as geek

typechars = ['S1', 'B', 'D', 'G', 'F', 'I', 'H', 'L', 'Q', 'S', 'U', 'V']

for typechar in typechars:
    print(typechar, ' : ', geek.typename(typechar))

# Python Program explaining
# numpy.put()

import numpy as geek

a = geek.arange(5)
geek.put(a, 22, -5, mode='clip')
print("After put : \n", a)

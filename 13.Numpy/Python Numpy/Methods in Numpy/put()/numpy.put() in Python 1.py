# Python Program explaining
# numpy.put()

import numpy as geek

a = geek.arange(5)
geek.put(a, [0, 2], [-44, -55])
print("After put : \n", a)

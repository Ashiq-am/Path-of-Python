import numpy as np

# using numpy.busday_count() method
gfg = np.busday_count('2019-09', '2019-10', weekmask ='Sat')

print(gfg)

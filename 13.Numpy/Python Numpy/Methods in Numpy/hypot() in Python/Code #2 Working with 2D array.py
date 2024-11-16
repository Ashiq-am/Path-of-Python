# Python3 program explaining
# hypot() function

import numpy as np

leg1 = np.random.rand(3, 4)
print ("leg1 array : \n", leg1)

leg2 = np.ones((3, 4))
print ("leg2 array : \n", leg2)

result = np.hypot(leg1, leg2)
print("\nHypotenuse is as follows :")
print(result)

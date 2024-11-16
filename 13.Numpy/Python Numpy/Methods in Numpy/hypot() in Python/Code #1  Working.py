# Python3 program explaining
# hypot() function

import numpy as np

leg1 = [12, 3, 4, 6]
print ("leg1 array : ", leg1)


leg2 = [5, 4, 3, 8]
print ("leg2 array : ", leg2)

result = np.hypot(leg1, leg2)
print("\nHypotenuse is as follows :")
print(result)

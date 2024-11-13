# Python code to demonstrate
# to calculate difference
# between adjacent elements in list

import numpy as np
# initialising _list
ini_list = np.array([5, 4, 89, 12, 32, 45])

# printing iniial_list
print("intial_list", str(ini_list))

# Calculating difference list
diff_list = np.diff(ini_list)

# printing difference list
print ("difference list: ", str(diff_list))

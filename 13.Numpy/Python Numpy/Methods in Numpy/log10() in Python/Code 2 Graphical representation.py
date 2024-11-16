# Python program showing
# Graphical representation of
# log10() function

import numpy as np
import matplotlib.pyplot as plt

in_array = [1, 2, 3, 4, 5]
out_array = np.log10(in_array)

print ("out_array : ", out_array)

plt.plot(in_array, in_array, color = 'blue', marker = "*")

# red for numpy.log10()
plt.plot(out_array, in_array, color = 'red', marker = "o")
plt.title("numpy.log10()")
plt.xlabel("out_array")
plt.ylabel("in_array")
plt.show()

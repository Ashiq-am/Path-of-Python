# Python program showing
# Graphical representation
# of arccos() function

import numpy as np
import matplotlib.pyplot as plt

in_array = np.linspace(-np.pi, np.pi, 12)
out_array1 = np.cos(in_array)
out_array2 = np.arccos(in_array)

print("in_array : ", in_array)
print("\nout_array with cos : ", out_array1)
print("\nout_arraywith arccos : ", out_array1)

# red for numpy.arccos()
plt.plot(in_array, out_array1,
         color='blue', marker="*")

plt.plot(in_array, out_array2,
         color='red', marker="o")

plt.title("blue : numpy.cos() \nred : numpy.arccos()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

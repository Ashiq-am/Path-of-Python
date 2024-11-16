# Python program showing
# Graphical representation of
# arcsin() function

import numpy as np
import matplotlib.pyplot as plt

in_array = np.linspace(-np.pi, np.pi, 12)
out_array1 = np.sin(in_array)
out_array2 = np.arcsin(in_array)

print("in_array : ", in_array)
print("\nout_array with sin : ", out_array1)
print("\nout_arraywith arcsin : ", out_array1)

# red for numpy.arcsin()
plt.plot(in_array, out_array1,
         color='blue', marker="*")

plt.plot(in_array, out_array2,
         color='red', marker="o")

plt.title("blue : numpy.sin() \nred : numpy.arcsin()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

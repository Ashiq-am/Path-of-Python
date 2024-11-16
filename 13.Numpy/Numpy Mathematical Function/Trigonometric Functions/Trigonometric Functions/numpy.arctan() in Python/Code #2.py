# Python program showing
# Graphical representation
# of arctan() function

import numpy as np
import matplotlib.pyplot as plt

in_array = np.linspace(-np.pi, np.pi, 12)
out_array1 = np.tan(in_array)
out_array2 = np.arctan(in_array)

print("in_array : ", in_array)
print("\nout_array with tan : ", out_array1)
print("\nout_arraywith arctan : ", out_array1)

# red for numpy.arccos()
plt.plot(in_array, out_array1,
         color='blue', marker="*")

plt.plot(in_array, out_array2,
         color='red', marker="o")

plt.title("blue : numpy.tan() \nred : numpy.arctan()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

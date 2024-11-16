# Python program showing
# Graphical representation of
# tan() function

import numpy as np
import matplotlib.pyplot as plt

in_array = np.linspace(0, np.pi, 12)
out_array = np.tan(in_array)

print("in_array : ", in_array)
print("\nout_array : ", out_array)

# red for numpy.tan()
plt.plot(in_array, out_array, color = 'red', marker = "o")
plt.title("numpy.tan()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

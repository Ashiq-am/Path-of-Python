# Python program showing
# Graphical representation
# of arctanh() function % matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

in_array = np.linspace(0.1, 0.99, 25)
out_array1 = np.tan(in_array)
out_array2 = np.arctanh(in_array)

print("in_array : ", in_array)
print("\nout_array with tan : ", out_array1)
print("\nout_array with arctanh : ", out_array2)
# blue for numpy.tanh()
# red for numpy.arctanh()
plt.plot(in_array, out_array1,
         color='blue', marker=".")

plt.plot(in_array, out_array2,
         color='red', marker="+")

plt.title("blue : numpy.tan() \nred : numpy.arctanh()")
plt.xlabel("X")
plt.ylabel("Y")

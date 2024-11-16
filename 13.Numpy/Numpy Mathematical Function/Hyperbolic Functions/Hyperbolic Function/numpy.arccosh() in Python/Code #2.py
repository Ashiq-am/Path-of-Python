# Python program showing
# Graphical representation
# of arccosh() function
import inline as inline
import matplotlib
matplotlib
inline
import numpy as np
import matplotlib.pyplot as plt

in_array = np.linspace(1, np.pi, 18)
out_array1 = np.cos(in_array)
out_array2 = np.arccosh(in_array)

print("in_array : ", in_array)
print("\nout_array with cos : ", out_array1)
print("\nout_array with arccosh : ", out_array2)
# blue for numpy.cosh()
# red for numpy.arccosh()
plt.plot(in_array, out_array1,
         color='blue', marker=".")

plt.plot(in_array, out_array2,
         color='red', marker="+")

plt.title("blue : numpy.cos() \nred : numpy.arccosh()")
plt.xlabel("X")
plt.ylabel("Y")

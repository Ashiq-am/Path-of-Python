# Python program showing
# Graphical representation
# of arcsinh() function % matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

in_array = np.linspace(1, np.pi, 18)
out_array1 = np.sin(in_array)
out_array2 = np.arcsinh(in_array)

print("in_array : ", in_array)
print("\nout_array with sin : ", out_array1)
print("\nout_array with arcsinh : ", out_array2)
# blue for numpy.sinh()
# red for numpy.arcsinh()
plt.plot(in_array, out_array1,
         color='blue', marker=".")

plt.plot(in_array, out_array2,
         color='red', marker="+")

plt.title("blue : numpy.sin() \nred : numpy.arcsinh()")
plt.xlabel("X")
plt.ylabel("Y")

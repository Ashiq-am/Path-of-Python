# Python code to implement
# the atanh()function
import math
import numpy as np
import matplotlib.pyplot as plt

in_array = np.linspace(-np.pi / 3.5, np.pi / 3.5, 10)

print("Input_Array : \n", in_array)

out_array = []

for i in range(len(in_array)):
    out_array.append(math.atanh(in_array[i]))
    i += 1

print("\nOutput_Array : \n", out_array)

plt.plot(in_array, out_array, "go:")
plt.title("math.atanh()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Python code implementation of
# the acos() function
import math
import numpy as np
import matplotlib.pyplot as plt

in_array = np.linspace(-(1 / 3.5 * np.pi), 1 / 3.5 * np.pi, 20)

out_array = []

for i in range(len(in_array)):
    out_array.append(math.acos(in_array[i]))
    i += 1

print("Input_Array : \n", in_array)
print("\nOutput_Array : \n", out_array)

plt.plot(in_array, out_array, "go-")
plt.title("math.acos()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

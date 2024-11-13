# Python code to implement
# the atan()function
import math
import numpy as np
import matplotlib.pyplot as plt

in_array = np.linspace(0, np.pi, 10)

out_array = []

for i in range(len(in_array)):
    out_array.append(math.atan(in_array[i]))
    i += 1

print("Input_Array : \n", in_array)
print("\nOutput_Array : \n", out_array)

plt.plot(in_array, out_array, "go:")
plt.title("math.atan()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

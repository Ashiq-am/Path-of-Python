# Python code implementation of
# the cosh() function
import math
import numpy as np
import matplotlib.pyplot as plt

in_array = np.linspace(1, np.pi ** 2, 30)

out_array = []

for i in range(len(in_array)):
    out_array.append(math.cosh(in_array[i]))
    i += 1

print("Input_Array : \n", in_array)
print("\nOutput_Array : \n", out_array)

plt.plot(in_array, out_array, "go-")
plt.title("math.cosh()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

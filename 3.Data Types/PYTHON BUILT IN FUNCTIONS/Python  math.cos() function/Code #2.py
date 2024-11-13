# Python program showing
# Graphical representation of
# cos() function
import math
import numpy as np
import matplotlib.pyplot as plt

in_array = np.linspace(-(2 * np.pi), 2 * np.pi, 20)

out_array = []

for i in range(len(in_array)):
	out_array.append(math.cos(in_array[i]))
	i += 1


print("in_array : ", in_array)
print("\nout_array : ", out_array)

# red for numpy.sin()
plt.plot(in_array, out_array, color = 'red', marker = "o")
plt.title("math.cos()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

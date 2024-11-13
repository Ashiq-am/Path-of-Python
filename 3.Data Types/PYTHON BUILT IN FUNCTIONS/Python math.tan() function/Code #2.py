# Python program showing
# Graphical representation of
# tan() function
import math
import numpy as np
import matplotlib.pyplot as plt

in_array = np.linspace(0, np.pi, 10)

out_array = []

for i in range(len(in_array)):
	out_array.append(math.tan(in_array[i]))
	i += 1


print("in_array : ", in_array)
print("\nout_array : ", out_array)

# red for numpy.sin()
plt.plot(in_array, out_array, color = 'red', marker = "o")
plt.title("math.tan()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

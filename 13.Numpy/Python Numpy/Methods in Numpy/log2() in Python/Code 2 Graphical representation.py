# Python program showing
# Graphical representation of
# log2() function
import numpy as np
import matplotlib.pyplot as plt

in_array = [1, 1.2, 1.4, 1.6, 1.8, 2]
out_array = np.log2(in_array)

print ("out_array : ", out_array)

plt.plot(in_array, in_array, color = 'blue', marker = "*")

# red for numpy.log2()
plt.plot(out_array, in_array, color = 'red', marker = "o")
plt.title("numpy.log2()")
plt.xlabel("out_array")
plt.ylabel("in_array")
plt.show()

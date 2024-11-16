# Python program showing
# Graphical representation of
# exp2() function
import numpy as np
import matplotlib.pyplot as plt

in_array = [1, 2, 3, 4, 5 ,6]
out_array = np.exp2(in_array)

print("out_array : ", out_array)

y = [1, 2, 3, 4, 5 ,6]
plt.plot(in_array, y, color = 'blue', marker = "*")

# red for numpy.exp2()
plt.plot(out_array, y, color = 'red', marker = "o")
plt.title("numpy.exp2()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

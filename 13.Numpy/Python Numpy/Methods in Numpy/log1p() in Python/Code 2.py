# Python program showing
# Graphical representation of
# log1p() function
import numpy as np
import matplotlib.pyplot as plt

in_array = [1, 1.2, 1.4, 1.6, 1.8, 2]
out_array = np.log1p(in_array)

print ("out_array : ", out_array)

y = [1, 1.2, 1.4, 1.6, 1.8, 2]
plt.plot(in_array, y, color = 'blue', marker = "*")

# red for numpy.log1xp()
plt.plot(out_array, y, color = 'red', marker = "o")
plt.title("numpy.log1p()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

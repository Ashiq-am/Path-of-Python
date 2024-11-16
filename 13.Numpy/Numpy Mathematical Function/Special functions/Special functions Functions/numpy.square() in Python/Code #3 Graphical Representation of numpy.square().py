# Python program explaining
# square () function

import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(start=-5, stop=5,
                num=6, endpoint=True)

print("Graphical Representation : \n", np.square(a))

plt.title("blue : with square\nred : without square")
plt.plot(a, np.square(a))

plt.plot(a, a, color='red')
plt.show()

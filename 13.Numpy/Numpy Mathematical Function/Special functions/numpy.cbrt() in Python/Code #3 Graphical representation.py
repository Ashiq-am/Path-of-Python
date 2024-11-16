# Python program explaining
# cbrt () function

import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(start=-5, stop=150,
                num=10, endpoint=True)

print("Graphical Representation : \n", np.cbrt(a))

plt.title("blue : with cbrt\nred : without cbrt")
plt.plot(a, np.cbrt(a))

plt.scatter(a, a, color='red')
plt.show()

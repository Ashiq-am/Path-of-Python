# Python program explaining
# absolute () function

import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(start=-5, stop=5,
                num=6, endpoint=True)

print("Graphical Representation : \n",
      np.absolute(a))

plt.title("blue : with absolute\nred : without absolute")
plt.plot(a, np.absolute(a))

plt.plot(a, a, color='red')
plt.show()

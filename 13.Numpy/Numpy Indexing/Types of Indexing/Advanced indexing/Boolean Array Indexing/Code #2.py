# You may wish to square the multiples of 40
import numpy as np

a = np.array([10, 40, 80, 50, 100])
print(a[a % 40 == 0] ** 2)
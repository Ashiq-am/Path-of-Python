# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.array([[1.22, 2.25, -3.21, 4.45, 5.56, 6],
				[-6.65, 5.55, 4.32, 3.33, 2.12, -1.05]])

# applying MaskedArray.__abs__() method
print(np.ma.MaskedArray.__abs__(gfg))

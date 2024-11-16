# Python program explaining
# numpy.rfind() function

import numpy as np

a = np.array(['geeks', 'for', 'geeks'])

# counting a substring
print(np.char.rfind(a, 'geek'))

# counting a substring
print(np.char.rfind(a, 'fo'))

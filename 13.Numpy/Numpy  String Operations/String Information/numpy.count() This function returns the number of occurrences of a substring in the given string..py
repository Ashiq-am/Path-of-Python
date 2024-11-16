# Python program explaining
# numpy.count() function

import numpy as np

a = np.array(['geeks', 'for', 'geeks'])

# counting a substring
print(np.char.count(a, 'geek'))

# counting a substring
print(np.char.count(a, 'fo'))
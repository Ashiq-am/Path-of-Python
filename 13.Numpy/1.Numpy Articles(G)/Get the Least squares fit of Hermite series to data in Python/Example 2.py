import numpy as np
from numpy.polynomial import hermite

# x - co ordinate
x = np.linspace(-10, 10, 50)

# defining the y - co ordinate using numpy random
y = x**4 - x + np.random.uniform(len(x))

# finding the least squares
c, stats = hermite.hermfit(x, y, 3, full=True)

print(f'The x coordinate array is \n{x}\n')
print(f'The y coordinate array is \n{y}\n')
print(f'The hermit coefficient are \n{c}\n')
print(f'The resultant array is \n{stats}\n')

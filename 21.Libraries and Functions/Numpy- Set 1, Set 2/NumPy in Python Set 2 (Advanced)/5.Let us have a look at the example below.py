import numpy as np
import matplotlib.pyplot as plt

# x co-ordinates
x = np.arange(0, 9)
A = np.array([x, np.ones(9)])

# linearly generated sequence
y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
# obtaining the parameters of regression line
w = np.linalg.lstsq(A.T, y)[0]

# plotting the line
line = w[0]*x + w[1] # regression line
plt.plot(x, line, 'r-')
plt.plot(x, y, 'o')
plt.show()











"""So, this leads to the conclusion of this series of NumPy tutorial.

NumPy is a widely used general purpose library which is at the core of many other computation 
libraries like scipy, scikit-learn, tensorflow, matplotlib, opencv, etc. 

Having a basic understanding of NumPy helps in dealing with other higher level libraries efficiently!"""

import numpy as np
import matplotlib.pyplot as plt

alphabets = ['A', 'B', 'C', 'D', 'E']

# randomly generated array
random_array = np.random.random((5, 5))

figure = plt.figure()
axes = figure.add_subplot(111)

# using the matshow() function
caxes = axes.matshow(random_array, interpolation ='nearest')
figure.colorbar(caxes)

axes.set_xticklabels(['']+alphabets)
axes.set_yticklabels(['']+alphabets)

plt.show()

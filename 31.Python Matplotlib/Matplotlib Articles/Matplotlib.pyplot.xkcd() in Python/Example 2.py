import numpy as np
import matplotlib.pyplot as plt

with plt.xkcd():
    plt.plot([1, 2, 3, 4], [5, 4, 9, 2])
    plt.title('matplotlib.pyplot.xkcd()')
    plt.axhline(y=0, color='k')

    plt.show()

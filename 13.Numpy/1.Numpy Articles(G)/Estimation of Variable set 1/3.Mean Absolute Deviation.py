# Mean Absolute Deviation

import numpy as np


def mad(data):
    return np.mean(np.absolute(
        data - np.mean(data)))


Sequence = [2, 4, 6, 8]

print("Mean Absolute Deviation : ", mad(Sequence))

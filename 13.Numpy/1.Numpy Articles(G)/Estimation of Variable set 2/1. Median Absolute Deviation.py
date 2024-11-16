# Median Absolute Deviation

import numpy as np


def mad(data):
    return np.median(np.absolute(
        data - np.median(data)))


Sequence = [2, 4, 10, 6, 8, 11]

print("Median Absolute Deviation : ", mad(Sequence))


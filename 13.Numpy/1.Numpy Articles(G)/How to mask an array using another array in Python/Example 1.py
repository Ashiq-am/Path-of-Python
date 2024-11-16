# importing the library
import numpy as np


# function to create masked array
from pygame import mask


def masking(ar1, ar2):
    # masking the array1 by using array2
    # where array2 mod 7 is true
    mask = np.ma.masked_where(ar2 % 7, ar1)
    return mask

# main function
if __name__ == '__main__':
    # creating two arrays
    x = np.array([1, 2, 4, 5, 7, 8, 9])
    y = np.array([10, 12, 14, 5, 7, 0, 13])

    # calling masking function to get
    # masked array
    masked = masking(x, y)

    # getting the values as 1-d array which
    # are non masked
    masked_array = np.ma.compressed(mask)

    # printing the resultant array after masking
    print(f'Masked Array is:{masked_array}')

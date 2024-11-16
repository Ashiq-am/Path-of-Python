# importing the library
import numpy as np


# function to create masked array
def masking(ar1, ar2):
    # creating the mask of array2 where
    # condition array2 mod 3 is true
    mask = np.ma.masked_where(ar2 % 3, ar2)

    # getting the mask of the array
    res_mask = np.ma.getmask(mask)

    # masking the array1 with the result
    # of mask of array2
    masked = np.ma.masked_array(ar1, mask=res_mask)

    return masked


# main function
if __name__ == '__main__':
    # creating two arrays
    x = np.array([1, 2, 4, 5, 7, 8, 9])
    y = np.array([10, 12, 14, 5, 7, 0, 12])

    # calling masking function to get masked
    # array
    masked = masking(x, y)
    masked_array = np.ma.compressed(masked)

    # printing the resultant array after masking
    print(f'Masked Array is:{masked_array}')

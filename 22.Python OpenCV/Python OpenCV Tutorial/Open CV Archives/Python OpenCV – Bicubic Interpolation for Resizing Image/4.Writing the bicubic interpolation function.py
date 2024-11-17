# Bicubic operation
import math
import sys
from tokenize import u

import numpy as np
from altair.vega import padding


def bicubic(img, ratio, a):
    # Get image size
    H, W, C = img.shape

    # Here H = Height, W = weight,
    # C = Number of channels if the
    # image is coloured.
    img = padding(img, H, W, C)

    # Create new image
    dH = math.floor(H * ratio)
    dW = math.floor(W * ratio)

    # Converting into matrix
    dst = np.zeros((dH, dW, 3))

    # np.zeroes generates a matrix
    # consisting only of zeroes
    # Here we initialize our answer
    # (dst) as zero

    h = 1 / ratio

    print('Start bicubic interpolation')
    print('It will take a little while...')
    inc = 0

    for c in range(C):
        for j in range(dH):
            for i in range(dW):
                # Getting the coordinates of the
                # nearby values
                x, y = i * h + 2, j * h + 2

                x1 = 1 + x - math.floor(x)
                x2 = x - math.floor(x)
                x3 = math.floor(x) + 1 - x
                x4 = math.floor(x) + 2 - x

                y1 = 1 + y - math.floor(y)
                y2 = y - math.floor(y)
                y3 = math.floor(y) + 1 - y
                y4 = math.floor(y) + 2 - y

                # Considering all nearby 16 values
                mat_l = np.matrix([[u(x1, a), u(x2, a), u(x3, a), u(x4, a)]])
                mat_m = np.matrix([[img[int(y - y1), int(x - x1), c],
                                    img[int(y - y2), int(x - x1), c],
                                    img[int(y + y3), int(x - x1), c],
                                    img[int(y + y4), int(x - x1), c]],
                                   [img[int(y - y1), int(x - x2), c],
                                    img[int(y - y2), int(x - x2), c],
                                    img[int(y + y3), int(x - x2), c],
                                    img[int(y + y4), int(x - x2), c]],
                                   [img[int(y - y1), int(x + x3), c],
                                    img[int(y - y2), int(x + x3), c],
                                    img[int(y + y3), int(x + x3), c],
                                    img[int(y + y4), int(x + x3), c]],
                                   [img[int(y - y1), int(x + x4), c],
                                    img[int(y - y2), int(x + x4), c],
                                    img[int(y + y3), int(x + x4), c],
                                    img[int(y + y4), int(x + x4), c]]])
                mat_r = np.matrix(
                    [[u(y1, a)], [u(y2, a)], [u(y3, a)], [u(y4, a)]])

                # Here the dot function is used to get the dot
                # product of 2 matrices
                dst[j, i, c] = np.dot(np.dot(mat_l, mat_m), mat_r)

    # If there is an error message, it
    # directly goes to stderr
    sys.stderr.write('\n')

    # Flushing the buffer
    sys.stderr.flush()
    return dst

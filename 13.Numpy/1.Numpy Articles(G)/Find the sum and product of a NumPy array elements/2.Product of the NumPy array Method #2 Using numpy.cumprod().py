# importing numpy
import numpy as np


def main():
    # initialising array
    print('Initialised array')
    gfg = np.array([[1, 2, 3], [4, 5, 6]])
    print('original array')
    print(gfg)

    # cumulative product of the array
    print(np.cumprod(gfg))

    # cumulative product of the array along
    # axis 1
    print(np.cumprod(gfg, axis=1))

    # initialising a 2x3 shape array
    b = np.array([[None, None, None], [None, None, None]])

    # finding cumprod and storing it in array
    np.cumprod(gfg, axis=1, out=b)

    # printing resultant array
    print(b)


if __name__ == "__main__":
    main()

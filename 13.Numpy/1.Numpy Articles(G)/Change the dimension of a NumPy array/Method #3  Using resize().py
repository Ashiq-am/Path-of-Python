# importing numpy
import numpy as np


def main():
    # initialise array
    gfg = np.arange(1, 10)
    print('initialised array')
    print(gfg)

    # resezed array with dimensions in
    # range of original array
    np.resize(gfg, (3, 3))
    print('3x3 array')
    print(gfg)

    # re array with dimensions larger than
    # original array
    np.resize(gfg, (4, 4))

    # extra spaces will be filled with repeated
    # copies of original array
    print('4x4 array')
    print(gfg)

    # resize array with dimensions larger than
    # original array
    gfg.resize(5, 5)

    # extra spaces will be filled with zeros
    print('5x5 array')
    print(gfg)


if __name__ == "__main__":
    main()

# importing numpy
import numpy as np


def main():
    # initialising array
    gfg = np.arange(1, 10)
    print('initialised array')
    print(gfg)

    # reshaping array into a 3x3 with order C
    print('3x3 order C array')
    print(np.reshape(gfg, (3, 3), order='C'))

    # reshaping array into a 3x3 with order F
    print('3x3 order F array')
    print(np.reshape(gfg, (3, 3), order='F'))

    # reshaping array into a 3x3 with order A
    print('3x3 order A array')
    print(np.reshape(gfg, (3, 3), order='A'))


if __name__ == "__main__":
    main()

# importing numpy
import numpy as np


def main():
    # initialising array
    print('Initialised array')
    gfg = np.array([[1, 2, 3], [4, 5, 6]])
    print(gfg)

    # product along row
    print(np.prod(gfg, axis=1))

    # product along column
    print(np.prod(gfg, axis=0))

    # sum of entire array
    print(np.prod(gfg))

    # use of out
    # initialise a array with same dimensions
    # of expected output to use OUT parameter
    b = np.array([0])  # np.int32)#.shape = 1
    print(np.prod(gfg, axis=1, out=b))

    # the output is stored in b
    print(b)

    # use of keepdim
    print('with axis parameter')

    # output array's dimension is same as specified
    # by the axis
    print(np.prod(gfg, axis=0, keepdims=True))

    # output consist of 3 columns
    print(np.prod(gfg, axis=1, keepdims=True))

    # output consist of 2 rows
    print('without axis parameter')
    print(np.prod(gfg, keepdims=True))

    # we initialise prodcut to a factor of 10
    # instead of 1
    print('using initial parameter in sum function')
    print(np.prod(gfg, initial=10))

    # False allowed to skip sum operation on column 1 and 2
    # that's why output is 1 which is default initial value
    print('using where parameter ')
    print(np.prod(gfg, axis=0, where=[True, False, False]))


if __name__ == "__main__":
    main()

# importing numpy
import numpy as np


def main():
    # initialising array
    print('Initialised array')
    gfg = np.array([[1, 2, 3], [4, 5, 6]])
    print(gfg)

    # sum along row
    print(np.sum(gfg, axis=1))

    # sum along column
    print(np.sum(gfg, axis=0))

    # sum of entire array
    print(np.sum(gfg))

    # use of out
    # initialise a array with same dimensions
    # of expected output to use OUT parameter
    b = np.array([0])  # np.int32)#.shape = 1
    print(np.sum(gfg, axis=1, out=b))

    # the output is stored in b
    print(b)

    # use of keepdim
    print('with axis parameter')

    # output array's dimension is same as specified
    # by the axis
    print(np.sum(gfg, axis=0, keepdims=True))

    # output consist of 3 columns
    print(np.sum(gfg, axis=1, keepdims=True))

    # output consist of 2 rows
    print('without axis parameter')
    print(np.sum(gfg, keepdims=True))

    # we added 100 to the actual result
    print('using initial parameter in sum function')
    print(np.sum(gfg, initial=100))

    # False allowed to skip sum operation on column 1 and 2
    # that's why output is 0 for them
    print('using where parameter ')
    print(np.sum(gfg, axis=0, where=[True, False, False]))


if __name__ == "__main__":
    main()

import numpy as np

ex1 = np.array([1, 4, -9, np.nan])
ex2 = np.array([1, 45, -2, np.nan, 3,
                -np.nan, 3, np.nan])


def approach_1(data):
    # here the input data, is a numpy ndarray

    # initialize the number of non-NaN elements
    # in data
    count = 0

    # loop over each entry of the data
    for entry in data:

        # check whether the entry is a non-NaN value
        # or not
        if not np.isnan(entry):
            # if not NaN, increment "count" by 1
            count += 1
    return count


print(approach_1(ex1))
print(approach_1(ex2))

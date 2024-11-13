import numpy


def n_length_combo(iterable, r):
    char = tuple(iterable)
    n = len(char)

    if r > n:
        return

    index = numpy.arange(r)

    # retruns the first sequence
    yield tuple(char[i] for i in index)

    while True:

        for i in reversed(range(r)):
            if index[i] != i + n - r:
                break
        else:
            return

        index[i] += 1

        for j in range(i + 1, r):
            index[j] = index[j - 1] + 1

        yield tuple(char[i] for i in index)

    # Driver code


print([x for x in n_length_combo("abc", 2)])

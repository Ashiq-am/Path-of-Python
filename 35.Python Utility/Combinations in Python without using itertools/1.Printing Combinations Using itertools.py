# Import combinations from itertools
from itertools import combinations


def n_length_combo(arr, n):
    # using set to deal
    # with duplicates
    return list(combinations(arr, n))


# Driver Function
if __name__ == "__main__":
    arr = 'abc'
    n = 2
    print(n_length_combo([x for x in arr], n))

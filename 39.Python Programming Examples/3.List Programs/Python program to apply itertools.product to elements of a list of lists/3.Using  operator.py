import itertools


def product(lst):
    # Unpack operation performed
    # by '*' operator and returning
    # the list containing cartesian
    # product
    return [x for x in itertools.product(*lst)]


# list of lists being passed in the method
print(product(["GfG", "GFG"]))

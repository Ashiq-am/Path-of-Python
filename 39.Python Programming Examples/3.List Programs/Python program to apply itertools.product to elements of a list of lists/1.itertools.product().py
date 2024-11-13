import itertools


def product(str1, str2):
    # returning the list containing
    # cartesian product
    return [x for x in itertools.product(list(str1),
                                         list(str2))]


print(product("GfG", "GFG"))

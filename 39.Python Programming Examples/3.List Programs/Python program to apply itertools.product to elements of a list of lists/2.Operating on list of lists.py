import itertools


def product(list_of_str):
    str1 = list_of_str[0]
    str2 = list_of_str[1]

    # returning the list
    # containing cartesian product
    return [x for x in itertools.product(list(str1),
                                         list(str2))]


print(product(["GfG", "GFG"]))

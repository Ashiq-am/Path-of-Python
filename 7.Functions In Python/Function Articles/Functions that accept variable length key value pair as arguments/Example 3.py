# using kwargs
# in functions
# to concatenate


def concatenate(**arguments):
    # initialising empty string
    final_str = ""

    # Iterating over the Python kwargs
    # dictionary
    for elements in arguments.values():
        final_str += elements
    return final_str


# driver code
if __name__ == '__main__':
    print(concatenate(a="g", b="F", c="g"))

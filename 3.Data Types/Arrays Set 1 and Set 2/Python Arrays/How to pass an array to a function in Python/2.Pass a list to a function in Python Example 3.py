# User defined function taking the
# values as input
def Product(*arguments):
    p = 1
    for i in arguments:
        # Multiplying each and every element
        p *= i

    # Printing the final answer which
    # is their multiplication
    print(p)


# Passing values that we want in our list
Product(4, 5, 1, 2)

# function to print the fraction of
# a given rational number
def reducedfraction(d):
    # function that converts a rational number
    # to the reduced fraction
    b = d.as_integer_ratio()

    # reduced the list that contains the fraction
    return b


# driver code
b = reducedfraction(2.5)
print(b[0], "/", b[1])

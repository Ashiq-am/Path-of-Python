# Python3 code to demonstrate working of
# Tuple as function arguments

# function with default arguments
def fnc(a=None, b=None):
    print("Value of a : " + str(a))
    print("Value of b : " + str(b))


# Driver code
if __name__ == "__main__":
    # initializing a And b


    a = 4
    b = 7

    # Tuple as function arguments
    # Case 1 - passing as integers


    print("The result of Case 1 : ")
    fnc(a, b)

    # Tuple as function arguments
    # Case 2 - Passing as tuple
    print("The result of Case 2 : ")
    fnc((a, b))

    # Tuple as function arguments
    # Case 3 - passing as pack/unpack
    # operator, as integer
    print("The result of Case 3 : ")
    fnc(*(a, b))

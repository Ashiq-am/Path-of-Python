# Program to Print a,
# Triangle Pattern using a string S.

def fun(S):
    # str variable to make a new string.
    str = ""

    # len variable to calculate the
    # length of the string.
    length = len(S);

    # Outer loop to control the rows.
    i = 0
    while (i < length):
        str = ""

        # First Inner loop to print
        # the dot character.
        j = 0
        while (j < i):
            str += "."
            j = j + 1

        # Second Inner loop to print
        # the remaining string,
        k = i
        while (k < length):
            str += S[k]
            k += 1

        # Printing the row and going
        # to the next line.
        print(str)

        # Incrementing the loop
        # control variable.
        i += 1


# Drivers code
S = "Geeks"

# Function call
fun(S)

# This code is contributed by akashish__
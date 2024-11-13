# Python code
# Triangle Pattern using a string S.
def fun(S):
    # str variable to make a new string.
    str = ""

    # len variable to calculate the length of the string.
    l = len(S)

    # Outer loop to control the rows.
    for i in range(0, l):

        str = ""

        # First Inner loop to pr the dot character.
        for j in range(0, i):
            str += "."

        # Second Inner loop to pr the remaining string,
        for j in range(i, l):
            str += S[j]

        # Pring the row and going to the next line.
        print(str)

# Drivers code
S = "Geeks"

# Function call
fun(S)



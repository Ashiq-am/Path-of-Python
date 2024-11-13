# Python3 program for the above approach

from itertools import permutations


# Function to convert binary
# string to equivalent decimal
def binToDec(n):
    num = n
    dec_value = 0

    # Initializing base
    # value to 1, i.e 2 ^ 0
    base1 = 1

    len1 = len(num)

    for i in range(len1 - 1, -1, -1):

        if (num[i] == '1'):
            dec_value += base1

        base1 = base1 * 2

    # Return the resultant
    # decimal number
    return dec_value


# Function to print all distinct
# decimals represented by the
# all permutations of the string
def printDecimal(permute):
    # Set to store distinct
    # decimal representations
    allDecimals = set()

    # Iterate over all permuations
    for i in permute:

        # Initilalize an empty string
        s = ""

        # Traverse the list
        for j in i:
            # Add each element
            # to the string
            s += j

        # Convert the current binary
        # representation to decimal
        result = binToDec(s)

        # Add the current decimal
        # value into the set
        allDecimals.add(result)

    # Print the distinct decimals
    print(allDecimals)


# Utility function to print all
# distinct decimal representations
# of all permutations of string
def totalPermutations(string):
    # Convert string to list
    lis = list(string)

    # Built in method to store all
    # the permuations of the list
    permutelist = permutations(lis)

    printDecimal(permutelist)


# Given binary string
binarystring = '1010'

# Function call to print all distinct
# decimal values represented by all
# permutations of the given string
totalPermutations(binarystring)

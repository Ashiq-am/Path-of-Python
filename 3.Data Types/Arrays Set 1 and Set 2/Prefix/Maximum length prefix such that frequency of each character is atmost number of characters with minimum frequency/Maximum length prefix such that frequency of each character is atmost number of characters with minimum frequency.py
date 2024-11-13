# Python3 implementation to find the
# prefix of the string such that
# occurrence of each character is
# atmost the count of minimum
# frequency in the string

# Function to find the maximum
# possible prefix of the string
def MaxPrefix(string):
    # Hash map to store the frequency
    # of the characters in the string
    Dict = {}
    maxprefix = 0

    # Iterate over the string to find
    # the occurrence of each Character
    for i in string:
        Dict[i] = Dict.get(i, 0) + 1

    # Minimum frequency of the Characters
    minfrequency = min(Dict.values())
    countminFrequency = 0

    # Loop to find the count of minimum
    # frequency in the hash-map
    for x in Dict:
        if (Dict[x] == minfrequency):
            countminFrequency += 1

    mapper = {}
    indi = 0

    # Loop to find the maximum possible
    # length of the prefix in the string
    for i in string:
        mapper[i] = mapper.get(i, 0) + 1

        # Condition to check if the frequency
        # is greater than minimum possible freq
        if (mapper[i] > countminFrequency):
            break
        indi += 1

    # maxprefix string and its length.
    print(string[:indi])


# Driver code
if __name__ == '__main__':
    # String is initialize.
    str = 'aabcdaab'
    # str is passed in MaxPrefix function.
    MaxPrefix(str)

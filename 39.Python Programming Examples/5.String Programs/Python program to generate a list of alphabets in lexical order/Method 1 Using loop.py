# function to get the list of alphabets
def generateAlphabetListDynamically(size=26):
    size = 26 if (size > 26 or size <= 0) else size

    # Empty list
    alphabetList = []

    # Looping from 0 to required size
    for i in range(size):
        alphabetList.append(chr(65 + i))

    # return the generated list
    return alphabetList

alphabetList = generateAlphabetListDynamically()
print('The alphabets in the list are:', *alphabetList)

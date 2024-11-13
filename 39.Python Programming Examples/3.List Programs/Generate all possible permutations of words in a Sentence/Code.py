# Python implementation of
# the above approach

from itertools import permutations


# Function to generate permutations
# of all words in a sentence
def calculatePermutations(sentence):
    # Stores all words in the sentence
    lis = list(sentence.split())

    # Stores all possible permuations
    # of words in this list
    permute = permutations(lis)

    # Iterate over all permutations
    for i in permute:

        # Convert the current
        # permutation into a list
        permutelist = list(i)

        # Print the words in the
        # list separated by spaces
        for j in permutelist:
            print(j, end=" ")

        # Print a new line
        print()


# Driver Code
if __name__ == '__main__':
    sentence = "sky is blue"
    calculatePermutations(sentence)

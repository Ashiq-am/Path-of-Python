# Python program for the above approach
from collections import Counter


# Python program to print words
# which occures k times
def printWords(sentence, k):
    # spliting the string
    lis = list(sentence.split(" "))

    # Calculating frequency of every word
    frequency = Counter(lis)

    # Traversing the frequency
    for i in frequency:

        # checking if frequency is k

        if (frequency[i] == k):
            # print the word
            print(i, end=" ")


# Driver code
# Given string
sentence = "sky is blue and my favourite color is blue"

# Given value of K
K = 2

printWords(sentence, K)


# Python program to implement
# the above approach

# Function to return the words which
# are common in both the sentences
def commonWords(sent1, sent2):
    # Splitting the words in a set
    sen1 = set(sent1)
    sen2 = set(sent2)

    # Stores the list of common words
    common = list(sen1.intersection(sen2))

    # Return the list
    return common


# Function to remove all the words
# that are common in both the strings
def removeCommonWords(sent1, sent2):
    # Stores the words of the
    # sentences in separate lists
    sentence1 = list(sent1.split())
    sentence2 = list(sent2.split())

    # Find the words that are
    # common in both the sentences
    commonlist = commonWords(sentence1,
                             sentence2)

    word = 0

    # Iterate the list of words
    # of the first sentence
    for i in range(len(sentence1)):

        # If word is common in both lists
        if sentence1[word] in commonlist:
            # Remove the word
            sentence1.pop(word)

            # Decrease the removed word
            word = word - 1
        word += 1

    word = 0

    # Iterate the list of words
    # of the second sentence
    for i in range(len(sentence2)):

        # If word is common in both lists
        if sentence2[word] in commonlist:
            # Remove the word
            sentence2.pop(word)

            # Decrease the removed word
            word = word - 1
        word += 1

    # Print the remaining words
    # in both the sentences
    print(*sentence1)
    print(*sentence2)


# Driver Code

S1 = "sky is blue in color"
S2 = "Raj likes sky blue color"

removeCommonWords(S1, S2)
